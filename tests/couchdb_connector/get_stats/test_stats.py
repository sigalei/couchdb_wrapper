from unittest.mock import patch

import pytest

from couch_wrapper.couchdb_connector import CouchDBConnectorBase
from tests.couchdb_connector import (CONNECTOR_PATH,
                                                         LOGGER_DEBUG_PATH)
# yapf: disable
from tests.couchdb_connector.get_stats import (
    STATS_TEST_CASES, STATS_TEST_CASES_PARAMS)

# yapf: enable


@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._get_database_documents')
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._set_document_timestamp')
@patch(CONNECTOR_PATH + '.CouchDBConnectorBase._get_database')
@patch(LOGGER_DEBUG_PATH)
@pytest.mark.parametrize(STATS_TEST_CASES_PARAMS, STATS_TEST_CASES)
def test_stats(_, __, ___, mocked_get_database_documents, documents,
               all_database_documents, expected_stats, force_insertion):
    mocked_get_database_documents.return_value = all_database_documents

    connector = CouchDBConnectorBase()

    connector.notify = True
    connector.force_insertion = force_insertion
    connector.update_timestamp = True
    connector.partial_update = False

    _ = connector._get_bulk(documents)

    assert connector.stats == expected_stats
