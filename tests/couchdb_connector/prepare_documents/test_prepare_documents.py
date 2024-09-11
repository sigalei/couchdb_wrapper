from unittest.mock import Mock, patch

import pytest

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import CONNECTOR_PATH
from tests.couchdb_connector.prepare_documents import (
    PREPARE_DOCUMENTS_TEST_CASES, PREPARE_DOCUMENTS_TEST_CASES_PARAMS)


# pylint: disable=too-many-arguments
@pytest.mark.parametrize(PREPARE_DOCUMENTS_TEST_CASES_PARAMS,
                         PREPARE_DOCUMENTS_TEST_CASES)
@patch(CONNECTOR_PATH + '.datetime')
@patch(CONNECTOR_PATH + '.pytz.timezone')
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._get_database')
def test_prepare_documents(_, mocked_pytz_timezone, mocked_datetime, document,
                           document_in_database, kwargs,
                           expected_prepared_document):
    mocked_datetime.now.return_value = Mock(isoformat=Mock(
        return_value='2019-10-10 08:53:30.082339+00:00'))

    connector = CouchDBConnectorBase(**kwargs)

    prepared_document = connector._prepare_document(document,
                                                    document_in_database)

    if expected_prepared_document:
        mocked_datetime.now.assert_called_once_with(
            tz=mocked_pytz_timezone.return_value)
        mocked_pytz_timezone.assert_called_once_with('America/Sao_Paulo')
        mocked_datetime.now.return_value.isoformat.assert_called_once_with(' ')

    assert prepared_document == expected_prepared_document
