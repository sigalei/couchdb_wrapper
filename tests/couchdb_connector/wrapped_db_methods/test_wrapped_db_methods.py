from unittest.mock import Mock, patch

import pytest

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import CONNECTOR_INIT_PATH


@pytest.mark.parametrize('method_name', ['get_view_result', 'all_docs'])
@patch(CONNECTOR_INIT_PATH, return_value=None)
def test_wrapped_db_methods(_, method_name):
    mocked_database = Mock()

    connector = CouchDBConnectorBase()
    connector.database = mocked_database

    mocked_args = [Mock(), Mock()]
    mocked_kwargs = {'arg1': Mock(), 'arg2': Mock()}

    connector.__getattribute__(method_name)(*mocked_args, **mocked_kwargs)
    mocked_database.__getattr__(method_name).assert_called_once_with(
        *mocked_args, **mocked_kwargs)
