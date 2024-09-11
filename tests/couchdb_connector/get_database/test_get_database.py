from unittest.mock import Mock, patch

import pytest

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import (CONNECTOR_INIT_PATH,
                                                         CONNECTOR_PATH,
                                                         LOGGER_ERROR_PATH,
                                                         OS_ENVIRON_PATH)
from tests.couchdb_connector.get_database import (
    GET_DATABASE_TEST_CASES, GET_DATABASE_TEST_CASES_PARAMS)


# pylint: disable=too-many-arguments
@pytest.mark.parametrize(GET_DATABASE_TEST_CASES_PARAMS,
                         GET_DATABASE_TEST_CASES)
@patch(LOGGER_ERROR_PATH)
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._get_server')
@patch(CONNECTOR_INIT_PATH, return_value=None)
def test_get_database(_, mocked_get_server, mocked_logger_error, has_server,
                      environment_vars, database_name, expected_exception_msg):
    mocked_database = Mock()
    mocked_url = Mock()
    connector = CouchDBConnectorBase()

    if has_server:
        mocked_get_server.return_value = {'test-db': mocked_database}
    else:
        mocked_get_server.return_value = None

    with patch(OS_ENVIRON_PATH, environment_vars):
        database = connector._get_database(mocked_url, database_name)
        mocked_get_server.assert_called_once_with(mocked_url)

        if not has_server:
            mocked_logger_error.assert_not_called()
            assert database is None
        elif not expected_exception_msg:
            assert database == mocked_database
            mocked_logger_error.assert_not_called()
        else:
            mocked_logger_error.assert_called_once_with(expected_exception_msg)
            assert database is None
