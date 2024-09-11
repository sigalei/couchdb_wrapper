import logging
import re
from collections import defaultdict
from datetime import datetime

import pytz
from cloudant import CouchDB
from requests.exceptions import HTTPError

from couch_wrapper.utils.environment import get_environment_variable
from couch_wrapper.utils.singleton import create_singleton

LOGGER = logging.getLogger('couch_wrapper.couchdb_connector')
SAVED_ITEMS = 'saved_items'
UPDATED_ITEMS = 'updated_items'
NOT_SAVED_ITEMS = 'not_saved_items'

DEFAULT_CLASSNAME = 'Item'

# pylint: disable=too-many-instance-attributes


class CouchDBConnectorBase():
    """
    CouchDBConnector is meant to be used at all data exchange with CouchDB.

    :param url: The url of the CouchDB server (if not passed, it is gotten
        from an environment variable called 'COUCH_URI')
    :param database_name: The name of the CouchDB database (if not passed,
        it is gotten from an environment variable called 'COUCH_DB_NAME')
    :param force_insertion: When True, the document is always saved as it
        is passed (no merge is done with the document already in database).
        Use this carefully and only when it is necessary.
    :param notify: Sets if the document will generate a notification
        to the clients.
    :param set_update_time: When False, the field 'UpdatedAt' will not be
        updated to current datetime. As 'UpdatedAt' relates more with
        extractions, batch scripts usually set this to False.
    :param partial_update: This should be set to True when the documents
        saved are partial ones (just the `_id` and some fields to be updated).
        You can't save partial documents with force insertion mode.
    :param merge_lists: If True, fields that are lists are merged with the
        lists that are already at database (without repetition).
    :param merge_fields: This is the list fields that will be merged if merge_lists
        is True. If None, all lists will be merged.
    """
    _COUCHDB_FIELDS = ['CreatedAt', 'UpdatedAt', 'Notify', '_rev', '_id']

    # pylint: disable=too-many-arguments
    def __init__(self,
                 url=None,
                 database_name=None,
                 force_insertion=False,
                 notify=True,
                 set_update_time=True,
                 partial_update=False,
                 merge_lists=False,
                 merge_fields=None):
        self.force_insertion = force_insertion
        self.notify = notify
        self.set_update_time = set_update_time
        self.partial_update = partial_update
        self.merge_lists = merge_lists
        self.merge_fields = merge_fields

        self.stats = defaultdict(lambda: {
            SAVED_ITEMS: 0,
            UPDATED_ITEMS: 0,
            NOT_SAVED_ITEMS: 0
        })

        self._check_arguments_conflict()

        self.database = self._get_database(url, database_name)

    def _check_arguments_conflict(self):
        if self.partial_update and self.force_insertion:
            error_msg = ('You can\'t save a partial document with force '
                         'insertion mode')
            raise ValueError(error_msg)

    def _get_database(self, url, database_name):
        server = self._get_server(url)
        if server is None:
            return None

        try:
            if not database_name:
                database_name = get_environment_variable('COUCH_DB_NAME')
            return server[database_name]
        except KeyError as error:
            log_msg = f'Database {str(error)} does not exists'
            LOGGER.error(log_msg)
        except AttributeError as error:
            log_msg = f'Could not find database: {str(error)}'
            LOGGER.error(log_msg)

    def _get_server(self, raw_url):
        try:
            if not raw_url:
                raw_url = get_environment_variable('COUCH_URI')
            url, username, password = self._get_credentials(raw_url)
            server = CouchDB(username,
                             password,
                             url=url,
                             connect=True,
                             auto_renew=True)
            server.r_session.headers.update({'Connection': 'close'})
            return server
        except (AttributeError, ConnectionError, HTTPError) as error:
            log_msg = f'Could not start Server: {str(error)}'
            LOGGER.error(log_msg)

    @staticmethod
    def _get_credentials(raw_url):
        credentials_re = (r'(?P<protocol>https?\:\/\/)'
                          r'(?P<username>.+)\:(?P<password>.+)'
                          r'\@(?P<url>.+)')
        credentials_match = re.match(credentials_re, raw_url)
        try:
            url = credentials_match.group(
                'protocol') + credentials_match.group('url')
            username = credentials_match.group('username')
            password = credentials_match.group('password')
            return url, username, password
        except AttributeError as error:
            raise AttributeError(f'Invalid server URL <{raw_url}>') from error

    def get_database_name(self):
        if self.database is not None:
            return self.database.database_name
        return None

    def get_document(self, document_id):
        if document_id in self.database:
            document = self.database[document_id]
            self.database.clear()
            return document
        return None

    def get_view_result(self, *args, **kwargs):
        return self.database.get_view_result(*args, **kwargs)

    def all_docs(self, *args, **kwargs):
        return self.database.all_docs(*args, **kwargs)

    def save(self, document):
        if document:
            responses = self.save_bulk([document])
            return responses[0] if responses else None
        return None

    def save_bulk(self, documents):
        bulk = self._get_bulk(documents)
        responses = self.database.bulk_docs(bulk)

        log_msg = f'Saved bulk of {len(bulk)} documents'
        LOGGER.debug(log_msg)

        return responses

    def _get_bulk(self, all_documents):
        bulk = []

        all_database_documents = self._get_database_documents(all_documents)
        for document, database_document in zip(all_documents,
                                               all_database_documents):
            prepared_document = self._prepare_document(document,
                                                       database_document)
            if not prepared_document:
                log_msg = f'Not saved: {document["_id"]}'
                LOGGER.debug(log_msg)
                continue
            log_msg = f'Saved document: {prepared_document["_id"]}'
            LOGGER.debug(log_msg)
            bulk.append(prepared_document)
        return bulk

    def _get_database_documents(self, all_documents):
        all_documents_ids = [document['_id'] for document in all_documents]

        db_docs_response = self.all_docs(keys=all_documents_ids,
                                         include_docs=True)
        all_db_documents = [
            db_document.get('doc') for db_document in db_docs_response['rows']
        ]

        return all_db_documents

    def _prepare_document(self, document, database_document):
        document_type = document.get('ClassName', DEFAULT_CLASSNAME)

        if database_document:
            document['_rev'] = database_document.get('_rev')
            document['CreatedAt'] = database_document.get('CreatedAt')
            document['UpdatedAt'] = database_document.get('UpdatedAt')
            # If force_insertion is False, we need to merge the current document
            # with the database document. But first, we check if the document is equal with
            # the database document, if they are equal we don't even need to save.
            if not self.force_insertion:
                if self._documents_are_equal(document, database_document):
                    self.stats[document_type][NOT_SAVED_ITEMS] += 1
                    return None
                if self.partial_update:
                    document = self.get_merge_documents_partial(
                        document, database_document)
                else:
                    document = self._get_merged_document(
                        document, database_document)
            self.stats[document_type][UPDATED_ITEMS] += 1
        else:
            self.stats[document_type][SAVED_ITEMS] += 1

        self._set_document_timestamp(document)
        document['Notify'] = self.notify
        return document

    def _documents_are_equal(self, document, database_document):
        for key, value in document.items():
            if key in self._COUCHDB_FIELDS:
                continue
            if database_document.get(key) != value:
                return False
        return True

    def get_merge_documents_partial(self, document, database_document):
        merged_document = database_document
        merged_fields = {}
        for field_name, document_field_value in document.items():
            database_document_value = database_document.get(field_name)
            if database_document_value:
                updated_document_field = self._merge_field(
                    database_document_value, document_field_value, field_name)
                merged_fields[field_name] = updated_document_field
        document.update(merged_fields)
        merged_document.update(document)
        return merged_document

    def _get_merged_document(self, document, database_document):
        merged_document = document
        for field_name, database_value in database_document.items():
            document_value = document.get(field_name)

            merged_value = self._merge_field(database_value, document_value,
                                             field_name)
            merged_document[field_name] = merged_value

        return merged_document

    def _merge_field(self, database_value, document_value, field_name):
        if isinstance(database_value, list) and self.merge_lists and \
            (self.merge_fields is None or field_name in self.merge_fields):
            merged_list = self._merge_lists(database_value, document_value)
            return merged_list
        return document_value

    @staticmethod
    def _merge_lists(database_list, document_list):
        merged_list = database_list
        if document_list:
            for item in document_list:
                if item not in database_list:
                    merged_list.append(item)

        return merged_list

    def delete_document(self, document_id):
        if document_id in self.database:
            self.database[document_id].delete()
            return True
        return None

    def _set_document_timestamp(self, document):
        timezone = 'America/Sao_Paulo'
        iso_timestamp = datetime.now(tz=pytz.timezone(timezone)).isoformat(' ')
        if not document.get('CreatedAt'):
            document['CreatedAt'] = iso_timestamp
        if not document.get('UpdatedAt') or self.set_update_time:
            document['UpdatedAt'] = iso_timestamp


CouchDBConnector = create_singleton(CouchDBConnectorBase)