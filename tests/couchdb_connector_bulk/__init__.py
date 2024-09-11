from unittest.mock import Mock, call

MOCKED_MAX_QUEUE_SIZE = 5


COUCHDB_CONNECTOR_BULK_SAVE_TEST_CASES_PARAMS = ('all_documents',
                                                 'save_bulk_documents_indices',
                                                 'remaining_queue_start_index')

COUCHDB_CONNECTOR_BULK_SAVE_TEST_CASES = [
    (
        [
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
        ],
        [
            (0, 5)
        ],
        5
    ),
    (
        [
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
        ],
        [
            (0, 5),
            (5, 10),
        ],
        10
    ),
    (
        [
            Mock(),
            Mock(),
        ],
        [],
        0
    ),
    (
        [],
        [],
        0
    ),
]
