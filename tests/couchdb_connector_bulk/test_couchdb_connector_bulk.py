from unittest.mock import Mock, call, patch

import pytest

from couch_wrapper.couchdb_connector_bulk import \
    CouchDBConnectorBulk
from tests.couchdb_connector_bulk import (
    COUCHDB_CONNECTOR_BULK_SAVE_TEST_CASES,
    COUCHDB_CONNECTOR_BULK_SAVE_TEST_CASES_PARAMS, MOCKED_MAX_QUEUE_SIZE)

COUCHDB_CONNECTOR_BULK_PATH = ('couch_wrapper.'
                               'couchdb_connector_bulk.')


@patch(COUCHDB_CONNECTOR_BULK_PATH + 'CouchDBConnector')
@pytest.mark.parametrize(('max_queue_size', 'expected_max_queue_size'), [
    (5, 5),
    (None, 100),
])
def test_couchdb_connector_bulk_init(mocked_couchdb_connector_class,
                                     max_queue_size, expected_max_queue_size):
    mocked_kwargs = {
        'url': 'https://couchdb.com/database/',
        'database_name': 'fake-database',
        'force_insertion': False,
        'notify': True
    }

    if max_queue_size is None:
        couchdb_connector_bulk = CouchDBConnectorBulk(**mocked_kwargs)
    else:
        couchdb_connector_bulk = CouchDBConnectorBulk(
            max_queue_size=max_queue_size, **mocked_kwargs)

    mocked_couchdb_connector_class.assert_called_once_with(**mocked_kwargs)

    expected_couchdb_connector = mocked_couchdb_connector_class.return_value
    assert couchdb_connector_bulk.couchdb_connector == \
           expected_couchdb_connector
    assert couchdb_connector_bulk.get_database_name == \
           expected_couchdb_connector.get_database_name

    assert couchdb_connector_bulk.documents_queue == []
    assert couchdb_connector_bulk.max_queue_size == expected_max_queue_size


@patch(COUCHDB_CONNECTOR_BULK_PATH + 'CouchDBConnectorBulk.__init__',
       return_value=None)
@pytest.mark.parametrize(COUCHDB_CONNECTOR_BULK_SAVE_TEST_CASES_PARAMS,
                         COUCHDB_CONNECTOR_BULK_SAVE_TEST_CASES)
def test_couchdb_connector_bulk_save(_, all_documents,
                                     save_bulk_documents_indices,
                                     remaining_queue_start_index):
    mocked_couchdb_connector = Mock()
    couchdb_connector_bulk = _get_couchdb_connector_bulk(
        [], mocked_couchdb_connector)

    for document in all_documents:
        couchdb_connector_bulk.save(document)

    expected_save_bulk_calls = _get_expected_save_bulk_calls(
        save_bulk_documents_indices, all_documents)

    mocked_save_bulk = mocked_couchdb_connector.save_bulk
    if expected_save_bulk_calls:
        mocked_save_bulk.assert_has_calls(expected_save_bulk_calls)
    else:
        mocked_save_bulk.assert_not_called()

    expected_remaining_queue = all_documents[remaining_queue_start_index:]

    assert couchdb_connector_bulk.documents_queue == expected_remaining_queue


def _get_couchdb_connector_bulk(documents_queue, mocked_couchdb_connector):
    couchdb_connector_bulk = CouchDBConnectorBulk()
    couchdb_connector_bulk.documents_queue = documents_queue
    couchdb_connector_bulk.max_queue_size = MOCKED_MAX_QUEUE_SIZE
    couchdb_connector_bulk.couchdb_connector = mocked_couchdb_connector
    return couchdb_connector_bulk


def _get_expected_save_bulk_calls(save_bulk_documents_indices, all_documents):
    expected_save_bulk_calls = []

    for start_index, end_index in save_bulk_documents_indices:
        expected_documents = all_documents[start_index:end_index]
        expected_call = call(expected_documents)
        expected_save_bulk_calls.append(expected_call)

    return expected_save_bulk_calls


@patch(COUCHDB_CONNECTOR_BULK_PATH + 'CouchDBConnectorBulk.__init__',
       return_value=None)
def test_couchdb_connector_bulk_del(_):
    mocked_couchdb_connector = Mock()
    couchdb_connector_bulk = _get_couchdb_connector_bulk(
        [], mocked_couchdb_connector)

    del couchdb_connector_bulk

    mocked_save_bulk = mocked_couchdb_connector.save_bulk
    mocked_save_bulk.assert_not_called()


@patch(COUCHDB_CONNECTOR_BULK_PATH + 'CouchDBConnectorBulk.__init__',
       return_value=None)
def test_couchdb_connector_bulk_del_with_one_doc(_):
    mocked_couchdb_connector = Mock()
    couchdb_connector_bulk = _get_couchdb_connector_bulk(
        [{}], mocked_couchdb_connector)

    documents_queue = couchdb_connector_bulk.documents_queue

    del couchdb_connector_bulk

    mocked_save_bulk = mocked_couchdb_connector.save_bulk
    mocked_save_bulk.assert_called_once_with(documents_queue)
