from unittest.mock import Mock, patch

import pytest

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector.init import assert_exception_msg
from tests.couchdb_connector import CONNECTOR_PATH


@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._get_database')
def test_init(mocked_get_database):
    mocked_url = Mock()
    mocked_database_name = Mock()
    mocked_notify = Mock()
    mocked_set_update_time = Mock()

    connector = CouchDBConnectorBase(url=mocked_url,
                                     database_name=mocked_database_name,
                                     force_insertion=False,
                                     notify=mocked_notify,
                                     set_update_time=mocked_set_update_time,
                                     partial_update=False)

    mocked_get_database.assert_called_once_with(mocked_url,
                                                mocked_database_name)
    assert connector.database == mocked_get_database.return_value
    assert connector.notify == mocked_notify
    assert connector.set_update_time == mocked_set_update_time


@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._get_database')
def test_init_default_values(mocked_get_database):
    connector = CouchDBConnectorBase()

    mocked_get_database.assert_called_once_with(None, None)
    assert connector.database == mocked_get_database.return_value
    assert connector.force_insertion is False
    assert connector.notify is True
    assert connector.set_update_time is True
    assert connector.partial_update is False


@pytest.mark.parametrize(
    ('force_insertion', 'partial_update', 'expected_exception'),
    [(True, True, True), (True, False, False), (False, True, False),
     (False, False, False)])
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._get_database')
def test_check_arguments_conflict(_, force_insertion, partial_update,
                                  expected_exception):
    if expected_exception:
        with pytest.raises(ValueError) as exception:
            CouchDBConnectorBase(force_insertion=force_insertion,
                                 partial_update=partial_update)
        expected_exception_msg = ('You can\'t save a partial document with '
                                  'force insertion mode')
        assert_exception_msg(exception, expected_exception_msg)
    else:
        connector = CouchDBConnectorBase(force_insertion=force_insertion,
                                         partial_update=partial_update)

        assert connector.force_insertion == force_insertion
        assert connector.partial_update == partial_update
