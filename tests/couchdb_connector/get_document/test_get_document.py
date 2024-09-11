from unittest.mock import patch

import pytest

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import CONNECTOR_INIT_PATH

MOCKED_DATABASE_DOCS = {
    'db_1': {
        '_id': 'db_1',
        '_rev': '1-7665fa768c0bc5d82a22e575f8d89571',
        'key': '1'
    },
    'db_2': {
        '_id': 'db_2',
        '_rev': '1-e4089027a88f46a62ccde155d47dd571',
        'key': '2'
    }
}


@pytest.mark.parametrize(('document_id', 'expected_document'),
                         [('db_1', MOCKED_DATABASE_DOCS['db_1']),
                          ('db_2', MOCKED_DATABASE_DOCS['db_2']),
                          ('db_3', None)])
@patch(CONNECTOR_INIT_PATH, return_value=None)
def test_get_document(_, document_id, expected_document):
    connector = CouchDBConnectorBase()
    connector.database = dict(MOCKED_DATABASE_DOCS)
    database_document = connector.get_document(document_id)

    assert database_document == expected_document

    if expected_document:
        assert connector.database == {}
