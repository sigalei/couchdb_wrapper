# pylint: disable=too-many-lines
PREPARE_DOCUMENTS_TEST_CASES_PARAMS = ('document', 'document_in_database',
                                       'kwargs', 'expected_prepared_document')

PREPARE_DOCUMENTS_TEST_CASES = [
    (
        {
            '_id': '1',
            "field_a": "valor_alterado"
        },
        {
            '_id': '1',
            "field_a": "valor_a",
            "field_b": "valor_b",
            "field_c": "valor_c"
        },
        {
            'force_insertion': False,
            'set_update_time': False,
            'merge_lists': False,
            'partial_update': True
        },
        {
            '_id': '1',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            '_rev': None,
            "field_a": "valor_alterado",
            "field_b": "valor_b",
            "field_c": "valor_c"
        }

    ),
    (
        {
            '_id': '1',
            "field_x": "valor_x"
        },
        {
            '_id': '1',
            "field_a": "valor_a",
            "field_b": "valor_b",
            "field_c": "valor_c"
        },
        {
            'force_insertion': False,
            'set_update_time': False,
            'merge_lists': False,
            'partial_update': True
        },
        {
            '_id': '1',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            '_rev': None,
            "field_a": "valor_a",
            "field_b": "valor_b",
            "field_c": "valor_c",
            "field_x": "valor_x"
        }
    ),
    (
        {
            '_id': '1',
            "field_x": "valor_x",
            "field_a": "valor_alterado"
        },
        {
            '_id': '1',
            "field_a": "valor_a",
            "field_b": "valor_b",
            "field_c": "valor_c"
        },
        {
            'force_insertion': False,
            'set_update_time': False,
            'merge_lists': False,
            'partial_update': True
        },
        {
            '_id': '1',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            '_rev': None,
            "field_a": "valor_alterado",
            "field_b": "valor_b",
            "field_c": "valor_c",
            "field_x": "valor_x"
        }

    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'IntField': 2,
            'Test2': 1,
            'List1' : ['test1', 'test3'],
            'List2' : ['test4', 'test5']
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1,
            'Test1' : 0,
            'List1' : ['test1', 'test2']
        },
        {
            'force_insertion': False,
            'set_update_time': True,
            'merge_lists': True,
            'partial_update': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'IntField': 2,
            'Test1': 0,
            'List1': ['test1', 'test2', 'test3'],
            '_rev': None,
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Test2': 1,
            'List2': ['test4', 'test5'],
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'IntField': None,
            'Test2': 1,
            'List1' : ['test1', 'test3'],
            'List2' : ['test4', 'test5']
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1,
            'Test1' : 0,
            'List1' : ['test1', 'test2']
        },
        {
            'force_insertion': False,
            'set_update_time': True,
            'merge_lists': False,
            'partial_update': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'IntField': None,
            'Test1': 0,
            'List1': ['test1', 'test3'],
            '_rev': None,
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Test2': 1,
            'List2': ['test4', 'test5'],
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1
        },
        None,
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1,
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1
        },
        None,
        {
            'force_insertion': True,
            'notify': False,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1,
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': False,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists and substitutes Notify',
            'BoolField': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists and substitutes Notify',
            'BoolField': False,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Field None substituted',
            'BoolField': None
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Field None substituted',
            'BoolField': None,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Documents are the same',
            'IntField': 12
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Documents are the same',
            'IntField': 12,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        None
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists and force_insertion is True',
            'BoolField': None
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Dummy text',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': True,
            'notify': False,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists and force_insertion is True',
            'BoolField': None,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields and notify false',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields and notify false',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields and notify false',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Document already has a (different) revision '
                            'number, but with force_insertion = True'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-854a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Document already has a (different) revision '
                            'number, but with force_insertion = True'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': True,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Document already has a (different) revision '
                            'number, but with force_insertion = True'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc'),
            'BoolField': False,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'DBField': '1',
            'DBField2': True
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc'),
            'BoolField': False,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'DBField': None,
            'DBField2': None
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc, and '
                            'the fields are all the same'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc, and '
                            'the fields are all the same'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'DBField': '1',
            'DBField2': True
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        None
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'There are nested fields in the document',
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            'Notify': True,
        },
        None,
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'There are nested fields in the document',
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('There are nested fields in the document, and the '
                            'id already exists'),
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            'Notify': True,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('There are nested fields in the document, and the '
                            'id already exists'),
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '4',
                'Field3': 3
            },
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-05 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-05 08:53:30.082339+00:00',
            'Notify': True,
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('There are nested fields in the document, and the '
                            'id already exists'),
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-05 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'There are more than one field different from DB',
            'BoolField': False,
            'DifferentField': 'hi',
            'DifferentNestedField': {
                'hi': 'bye'
            },
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            'Notify': True,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'There are more than one field different from DB',
            'DifferentField': 'bye',
            'DifferentNestedField': {
                'hi': 'hello'
            },
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-05 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-05 08:53:30.082339+00:00',
            'Notify': True,
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'There are more than one field different from DB',
            'BoolField': False,
            'DifferentField': 'hi',
            'DifferentNestedField': {
                'hi': 'bye'
            },
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-05 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
        }
    ),
    # From here all 'set_update_time' are False ("UpdatedAt" are let alone if
    # it exists).
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1
        },
        None,
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1,
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1
        },
        None,
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1,
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1
        },
        None,
        {
            'force_insertion': True,
            'notify': False,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document doesn\'t exist in database',
            'IntField': 1,
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': False,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists and substitutes Notify',
            'BoolField': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists and substitutes Notify',
            'BoolField': False,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': False,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Field None substituted',
            'BoolField': None
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Document exists in the database',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Field None substituted',
            'BoolField': None,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Documents are the same',
            'IntField': 12
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Documents are the same',
            'IntField': 12,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        None
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields and notify false',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields and notify false',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'Same document with more fields and notify false',
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': False,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Document already has a (different) revision '
                            'number, but with force_insertion = True'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-854a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Document already has a (different) revision '
                            'number, but with force_insertion = True'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': True,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Document already has a (different) revision '
                            'number, but with force_insertion = True'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'NewField': '1',
            'NewField2': '2'
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc'),
            'BoolField': False,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'DBField': '1',
            'DBField2': True
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc'),
            'BoolField': False,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'DBField': None,
            'DBField2': None
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc, and '
                            'the fields are all the same'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('Database doc with more fields than the doc, and '
                            'the fields are all the same'),
            'BoolField': True,
            'CreatedAt': '2019-10-08 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-09 08:53:30.082339+00:00',
            'Notify': True,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'DBField': '1',
            'DBField2': True
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        None
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('There are nested fields in the document, and the '
                            'id already exists'),
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            'Notify': True,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('There are nested fields in the document, and the '
                            'id already exists'),
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '4',
                'Field3': 3
            },
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-05 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-05 08:53:30.082339+00:00',
            'Notify': True,
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': ('There are nested fields in the document, and the '
                            'id already exists'),
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-05 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-05 08:53:30.082339+00:00',
            'Notify': True,
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'There are more than one field different from DB',
            'BoolField': False,
            'DifferentField': 'hi',
            'DifferentNestedField': {
                'hi': 'bye'
            },
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            'Notify': True,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'There are more than one field different from DB',
            'DifferentField': 'bye',
            'DifferentNestedField': {
                'hi': 'hello'
            },
            'BoolField': False,
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-05 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-05 08:53:30.082339+00:00',
            'Notify': True,
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': False,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'Explanation': 'There are more than one field different from DB',
            'BoolField': False,
            'DifferentField': 'hi',
            'DifferentNestedField': {
                'hi': 'bye'
            },
            'NestedField': {
                'Field1': True,
                'Field2': '1',
                'Field3': 3
            },
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-05 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-05 08:53:30.082339+00:00',
            'Notify': True,
        }
    ),
    # The next test cases test the behavior of merge_lists. When set to True,
    # _get_merged_document concatenates list on the database with the list
    # on the new document version
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': False
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2', 'new_value'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': [],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2
        },
        None,
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2,
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': None,
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': [],
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': False,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': False
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'new_value', 'old_value2'],
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2', 'new_value'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1'],
            'IntField': 2,
            'test_value' : None
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'test_value' : 1
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True,
            'test_value' : None
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value1', 'new_value2'],
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value1', 'new_value2'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'IntField': 1,
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': True,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'IntField': 2,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True
        }
    ),
    (
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['new_value'],
            'StrListField2': ['new_value'],
            'IntField': 2,
            'StrField': None,
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2'],
            'StrListField2': ['old_value1', 'old_value2'],
            'IntField': 4,
            'StrField': 'String',
            '_rev': '1-967a00dff5e02add41819138abb3284d'
        },
        {
            'force_insertion': False,
            'notify': True,
            'set_update_time': True,
            'merge_lists': True,
            'merge_fields': ['StrListField']
        },
        {
            '_id': '1',
            'ClassName': 'sl_item',
            'StrListField': ['old_value1', 'old_value2', 'new_value'],
            'StrListField2': ['new_value'],
            'IntField': 2,
            'StrField': None,
            '_rev': '1-967a00dff5e02add41819138abb3284d',
            'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
            'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
            'Notify': True
        }
    )
]
