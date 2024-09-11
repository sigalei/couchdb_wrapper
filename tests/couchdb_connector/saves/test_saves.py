from unittest.mock import Mock, patch

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import (CONNECTOR_INIT_PATH,
                                                         CONNECTOR_PATH)


@patch(CONNECTOR_PATH + '.CouchDBConnectorBase.save_bulk')
@patch(CONNECTOR_INIT_PATH, return_value=None)
def test_save(_, mocked_save_bulk):
    mocked_document = Mock()
    mocked_response = Mock()
    mocked_save_bulk.return_value = [mocked_response]
    connector = CouchDBConnectorBase()

    # Document was inserted or updated
    response = connector.save(mocked_document)
    mocked_save_bulk.assert_called_once_with([mocked_document])
    assert response == mocked_response

    # Document was not saved since it was the same as the database one
    mocked_save_bulk.reset_mock()
    mocked_save_bulk.return_value = []
    response = connector.save(mocked_document)
    mocked_save_bulk.assert_called_once_with([mocked_document])
    assert response is None

    # No document
    mocked_save_bulk.reset_mock()
    response = connector.save(None)
    mocked_save_bulk.assert_not_called()
    assert response is None


@patch(CONNECTOR_INIT_PATH, return_value=None)
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._get_bulk')
def test_save_bulk(mocked_get_bulk, _):
    mocked_database = Mock()
    mocked_documents = Mock()

    connector = CouchDBConnectorBase()
    connector.database = mocked_database

    responses = connector.save_bulk(mocked_documents)

    mocked_get_bulk.assert_called_once_with(mocked_documents)

    mocked_bulk = mocked_get_bulk.return_value
    mocked_database.bulk_docs.assert_called_once_with(mocked_bulk)

    mocked_responses = mocked_database.bulk_docs.return_value
    assert responses == mocked_responses
