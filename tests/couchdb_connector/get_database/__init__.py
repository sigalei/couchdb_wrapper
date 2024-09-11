GET_DATABASE_TEST_CASES_PARAMS = ('has_server', 'environment_vars',
                                  'database_name', 'expected_exception_msg')
GET_DATABASE_TEST_CASES = [
    (
        True,
        {
            'COUCH_DB_NAME': 'test-db'
        },
        None,
        None
    ),
    (
        True,
        {},
        'test-db',
        None
    ),
    (
        True,
        {},
        None,
        ('Could not find database: '
         'Environment variable COUCH_DB_NAME could not be found')
    ),
    (
        True,
        {
            'WRONG_ENV': 'test-db'
        },
        None,
        ('Could not find database: '
         'Environment variable COUCH_DB_NAME could not be found')
    ),
    (
        True,
        {
            'COUCH_DB_NAME': 'wrong_database_name'
        },
        None,
        'Database \'wrong_database_name\' does not exists'
    ),
    (
        True,
        {},
        'wrong_database_name',
        'Database \'wrong_database_name\' does not exists'
    ),
    (
        False,
        {},
        'test-db',
        None,
    )
]
