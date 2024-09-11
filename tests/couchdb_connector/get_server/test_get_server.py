from unittest.mock import Mock, patch

import pytest

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import (CONNECTOR_INIT_PATH,
                                                         CONNECTOR_PATH,
                                                         LOGGER_ERROR_PATH,
                                                         OS_ENVIRON_PATH)
from tests.couchdb_connector.get_server import (
    GET_SERVER_TEST_CASES, GET_SERVER_TEST_CASES_PARAMS)


# pylint: disable=too-many-arguments
@pytest.mark.parametrize(GET_SERVER_TEST_CASES_PARAMS, GET_SERVER_TEST_CASES)
@patch(LOGGER_ERROR_PATH)
@patch(CONNECTOR_INIT_PATH, return_value=None)
def test_get_server(_, mocked_logger_error, couchdb_exception,
                    environment_vars, url, expected_username,
                    expected_password, expected_url, expected_exception_msg):
    mocked_server = Mock()
    with patch(OS_ENVIRON_PATH, environment_vars):
        with patch(CONNECTOR_PATH + '.CouchDB',
                   side_effect=_mocked_couchdb_factory(
                       couchdb_exception, mocked_server)) as mocked_couchdb:
            connector = CouchDBConnectorBase()
            server = connector._get_server(url)
            if not expected_exception_msg or couchdb_exception:
                mocked_couchdb.assert_called_once_with(expected_username,
                                                       expected_password,
                                                       url=expected_url,
                                                       connect=True,
                                                       auto_renew=True)
            if not expected_exception_msg:
                assert server == mocked_server
                mocked_logger_error.assert_not_called()
            else:
                mocked_logger_error.assert_called_once_with(
                    expected_exception_msg)
                assert server is None


def _mocked_couchdb_factory(exception, mocked_server):
    # pylint:disable=unused-argument
    def mocked_couchdb(*args, **kwargs):
        if exception:
            raise exception
        return mocked_server

    return mocked_couchdb
