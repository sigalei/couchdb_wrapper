from requests.exceptions import HTTPError, MissingSchema

GET_SERVER_TEST_CASES_PARAMS = ('couchdb_exception', 'environment_vars', 'url',
                                'expected_username', 'expected_password',
                                'expected_url', 'expected_exception_msg')

GET_SERVER_TEST_CASES = [
    (
        None,
        {
            'COUCH_URI': 'http://admin:admin@localhost:5984'
        },
        None,
        'admin',
        'admin',
        'http://localhost:5984',
        None
    ),
    (
        None,
        {
            'COUCH_URI': 'https://jjadjdSdk482137:_923*\\dsjf@example1.com'
        },
        None,
        'jjadjdSdk482137',
        '_923*\\dsjf',
        'https://example1.com',
        None
    ),
    (
        None,
        {
            'COUCH_URI': 'https://jjadjdSdk482137:_923*\\dsjf@example1.com'
        },
        'https://default_user:default_password@couchdb-local.net',
        'default_user',
        'default_password',
        'https://couchdb-local.net',
        None
    ),
    (
        None,
        {},
        'https://default_password@couchdb-local.net',
        None,
        None,
        None,
        ('Could not start Server: Invalid server URL '
         '<https://default_password@couchdb-local.net>')
    ),
    (
        None,
        {
            'COUCH_URI': 'https://default_password@couchdb-local.net'
        },
        None,
        None,
        None,
        None,
        ('Could not start Server: Invalid server URL '
         '<https://default_password@couchdb-local.net>')
    ),
    (
        None,
        {},
        None,
        None,
        None,
        None,
        ('Could not start Server: Environment variable COUCH_URI '
         'could not be found')
    ),
    (
        None,
        {},
        'http://admin:admin@localhost:5984',
        'admin',
        'admin',
        'http://localhost:5984',
        None
    ),
    (
        None,
        {
            'COUCH_URI': None
        },
        None,
        None,
        None,
        None,
        ('Could not start Server: Environment variable COUCH_URI '
         'could not be found')
    ),
    (
        ConnectionError('HTTPConnectionPool(host=\'localhoasdst\', port=5984)'
                        ': Max retries exceeded with url: /_session (Caused '
                        'by NewConnectionError(\'<urllib3.connection.'
                        'HTTPConnection object at 0x7f46dd47eed0>: Failed to '
                        'establish a new connection: [Errno -2] Name or '
                        'service not known\'))'),
        {
            'COUCH_URI': 'http://admin:admin@localhostz:5984'
        },
        None,
        'admin',
        'admin',
        'http://localhostz:5984',
        ('Could not start Server: HTTPConnectionPool(host=\'localhoasdst\', '
         'port=5984): Max retries exceeded with url: /_session (Caused '
         'by NewConnectionError(\'<urllib3.connection.HTTPConnection object '
         'at 0x7f46dd47eed0>: Failed to establish a new connection: '
         '[Errno -2] Name or service not known\'))')
    ),
    (
        HTTPError('401 Client Error: Unauthorized for url: '
                  'http://localhost:5984/_session'),
        {
            'COUCH_URI': ''
        },
        'http://admin:wrong_password@localhost:5984',
        'admin',
        'wrong_password',
        'http://localhost:5984',
        ('Could not start Server: 401 Client Error: Unauthorized for url: '
         'http://localhost:5984/_session')
    )
]
