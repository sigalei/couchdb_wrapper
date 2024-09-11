from unittest.mock import Mock, patch

import pytest

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import CONNECTOR_INIT_PATH


@patch(CONNECTOR_INIT_PATH, return_value=None)
@pytest.mark.parametrize(
    ('database', 'expected_database_name'),
    [(None, None), (Mock(database_name='db_name'), 'db_name'),
     (Mock(database_name='other_db_name'), 'other_db_name')])
def test_get_database_name(_, database, expected_database_name):
    connector = CouchDBConnectorBase()
    connector.database = database

    database_name = connector.get_database_name()

    assert database_name == expected_database_name
