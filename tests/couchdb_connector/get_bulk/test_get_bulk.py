from unittest.mock import patch

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import (CONNECTOR_INIT_PATH,
                                                         CONNECTOR_PATH,
                                                         LOGGER_DEBUG_PATH)

from . import (ALL_MOCKED_DOCUMENTS, EXPECTED_BULK,
               EXPECTED_PREPARED_DOCUMENTS_CALLS, MOCKED_DB_RESPONSE,
               MOCKED_PREPARED_DOCUMENTS)


@patch(CONNECTOR_INIT_PATH, return_value=None)
@patch(LOGGER_DEBUG_PATH)
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase.all_docs')
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._prepare_document')
def test_get_bulk_empty_list(mocked_prepare_document, mocked_all_docs, *_):
    mocked_all_docs.return_value = {'rows': []}

    connector = CouchDBConnectorBase()
    bulk = connector._get_bulk([])

    mocked_all_docs.assert_called_once_with(keys=[], include_docs=True)
    mocked_prepare_document.assert_not_called()

    assert bulk == []


@patch(CONNECTOR_INIT_PATH, return_value=None)
@patch(LOGGER_DEBUG_PATH)
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase.all_docs')
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._prepare_document')
def test_get_bulk_non_empty_list(mocked_prepare_document, mocked_all_docs, *_):
    mocked_all_docs.return_value = MOCKED_DB_RESPONSE
    mocked_prepare_document.side_effect = MOCKED_PREPARED_DOCUMENTS

    connector = CouchDBConnectorBase()
    bulk = connector._get_bulk(ALL_MOCKED_DOCUMENTS)

    expected_all_documents_ids = ['1', '2', '3']
    mocked_all_docs.assert_called_once_with(keys=expected_all_documents_ids,
                                            include_docs=True)
    mocked_prepare_document.assert_has_calls(EXPECTED_PREPARED_DOCUMENTS_CALLS)

    assert bulk == EXPECTED_BULK
