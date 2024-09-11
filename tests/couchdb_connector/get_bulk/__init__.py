from unittest.mock import call

ALL_MOCKED_DOCUMENTS = [
    {
        '_id': '1',
        'Field': 'value1'
    },
    {
        '_id': '2',
        'Field': 'value2'
    },
    {
        '_id': '3',
        'Field': 'value3'
    }
]

MOCKED_DB_RESPONSE = {
    'rows': [
        {
            'key': '1',
            'doc': {
                '_id': '1',
                'Field': 'db_value1'
            }
        },
        {
            'key': '2',
            'doc': {
                '_id': '2',
                'Field': 'value2'
            }
        },
        {
            'key': '3',
            'error': 'not_found'
        }
    ]
}

EXPECTED_PREPARED_DOCUMENTS_CALLS = [
    call(
        {
            '_id': '1',
            'Field': 'value1'
        },
        {
            '_id': '1',
            'Field': 'db_value1'
        }
    ),
    call(
        {
            '_id': '2',
            'Field': 'value2'
        },
        {
            '_id': '2',
            'Field': 'value2'
        }
    ),
    call(
        {
            '_id': '3',
            'Field': 'value3'
        },
        None
    )
]

MOCKED_PREPARED_DOCUMENTS = [
    {
        '_id': '1',
        'Field': 'value1',
        'CreadedAt': 'date'
    },
    None,
    {
        '_id': '3',
        'Field': 'value3',
        'CreadedAt': 'date'
    }
]

EXPECTED_BULK = [MOCKED_PREPARED_DOCUMENTS[0], MOCKED_PREPARED_DOCUMENTS[2]]
