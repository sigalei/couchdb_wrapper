STATS_TEST_CASES_PARAMS = ('documents', 'all_database_documents',
                           'expected_stats', 'force_insertion')
STATS_TEST_CASES = [
    (
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'prepare_document will return None')
            },
            {
                '_id': '2',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the saved items field'
            },
            {
                '_id': '3',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the saved items field',
                'AnotherField': 'dummy text',
                'BoolField': True
            },
            {
                '_id': '4',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the saved items field',
                'NestedField': {'ok': 'ok'}
            },
            {
                '_id': '5',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the updated items',
                'DifferentField': True
            }
        ],
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'prepare_document will return None'),
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
                '_rev': '123871283'
            },
            None,
            None,
            None,
            {
                '_id': '5',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the updated items',
                '_rev': '82738273',
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00'
            }
        ],
        {
            'sl_bill':{
                'saved_items': 3,
                'updated_items': 1,
                'not_saved_items': 1
            }
        },
        False
    ),
    # same as the first test but with force_insertion = True
    (
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'but will go to updated items because of '
                                'force_insertion')
            },
            {
                '_id': '2',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the saved items field'
            },
            {
                '_id': '3',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the saved items field',
                'AnotherField': 'dummy text',
                'BoolField': True
            },
            {
                '_id': '4',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the saved items field',
                'NestedField': {'ok': 'ok'}
            },
            {
                '_id': '5',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the updated items',
                'DifferentField': True
            }
        ],
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'but will go to updated items because of '
                                'force_insertion'),
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
                '_rev': '123871283'
            },
            None,
            None,
            None,
            {
                '_id': '5',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the updated items',
                '_rev': '82738273',
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00'
            }
        ],
        {
            'sl_bill': {
                'saved_items': 3,
                'updated_items': 2,
                'not_saved_items': 0
            }
        },
        True
    ),
    (
        [],
        [],
        {},
        False
    ),
    # Items of multiple types
    (
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'prepare_document will return None')
            },
            {
                '_id': '2',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the updated items field',
                'NestedField': {'key': 'new_value'}
            },
            {
                '_id': '3',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the saved items field',
                'AnotherField': 'dummy text',
                'BoolField': True
            },
            {
                '_id': '4',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the saved items field',
                'NestedField': {'ok': 'ok'}
            },
            {
                '_id': '5',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the updated items',
                'DifferentField': True
            },
            {
                '_id': '6',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the saved items',
                'DifferentField': True
            },
        ],
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'prepare_document will return None'),
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
                '_rev': '123871283'
            },
            {
                '_id': '2',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the updated items field',
                'NestedField': {'key': 'old_value'},
                '_rev': '132117899',
                'CreatedAt': '2020-04-15 08:53:30.082339+00:00',
                'UpdatedAt': '2020-05-07 11:05:30.046897+00:00'
            },
            None,
            None,
            {
                '_id': '5',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the updated items',
                '_rev': '82738273',
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00'
            },
            None,
        ],
        {
            'sl_bill': {
                'saved_items': 1,
                'updated_items': 1,
                'not_saved_items': 1
            },
            'sl_action': {
                'saved_items': 2,
                'updated_items': 1,
                'not_saved_items': 0
            },
        },
        False
    ),
    # items of multiple types with force_insertion=True
    (
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'but will update because of force insertion')
            },
            {
                '_id': '2',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the updated items field',
                'NestedField': {'key': 'new_value'}
            },
            {
                '_id': '3',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the saved items field',
                'AnotherField': 'dummy text',
                'BoolField': True
            },
            {
                '_id': '4',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the saved items field',
                'NestedField': {'ok': 'ok'}
            },
            {
                '_id': '5',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the updated items',
                'DifferentField': True
            },
            {
                '_id': '6',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the saved items',
                'DifferentField': True
            },
        ],
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'but will update because of force insertion'),
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
                '_rev': '123871283'
            },
            {
                '_id': '2',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the updated items field',
                'NestedField': {'key': 'old_value'},
                '_rev': '132117899',
                'CreatedAt': '2020-04-15 08:53:30.082339+00:00',
                'UpdatedAt': '2020-05-07 11:05:30.046897+00:00'
            },
            None,
            None,
            {
                '_id': '5',
                'ClassName': 'sl_bill',
                'Explanation': 'It will be added to the updated items',
                '_rev': '82738273',
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00'
            },
            None,
        ],
        {
            'sl_bill': {
                'saved_items': 1,
                'updated_items': 2,
                'not_saved_items': 0
            },
            'sl_action': {
                'saved_items': 2,
                'updated_items': 1,
                'not_saved_items': 0
            },
        },
        True
    ),
    # Partial items without "ClassName"
    (
        [
            {
                '_id': '1',
                'Explanation': ('the non standard fields are equal, '
                                'prepare_document will return None')
            },
            {
                '_id': '2',
                'Explanation': 'It will be added to the saved items field'
            },
            {
                '_id': '3',
                'Explanation': 'It will be added to the saved items field',
                'AnotherField': 'dummy text',
                'BoolField': True
            },
            {
                '_id': '4',
                'Explanation': 'It will be added to the saved items field',
                'NestedField': {'ok': 'ok'}
            },
            {
                '_id': '5',
                'Explanation': 'It will be added to the updated items',
                'DifferentField': True
            }
        ],
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'prepare_document will return None'),
                'FieldAtDB': True,
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
                '_rev': '123871283'
            },
            None,
            None,
            None,
            {
                '_id': '5',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the updated items',
                'FieldAtDB': False,
                '_rev': '82738273',
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00'
            }
        ],
        {
            'Item': {
                'saved_items': 3,
                'updated_items': 1,
                'not_saved_items': 1
            }
        },
        False
    ),
    # Partial items without "ClassName" and force_insertion=True
    (
        [
            {
                '_id': '1',
                'Explanation': ('the non standard fields are equal, '
                                'prepare_document will return None')
            },
            {
                '_id': '2',
                'Explanation': 'It will be added to the saved items field'
            },
            {
                '_id': '3',
                'Explanation': 'It will be added to the saved items field',
                'AnotherField': 'dummy text',
                'BoolField': True
            },
            {
                '_id': '4',
                'Explanation': 'It will be added to the saved items field',
                'NestedField': {'ok': 'ok'}
            },
            {
                '_id': '5',
                'Explanation': 'It will be added to the updated items',
                'DifferentField': True
            }
        ],
        [
            {
                '_id': '1',
                'ClassName': 'sl_bill',
                'Explanation': ('the non standard fields are equal, '
                                'prepare_document will return None'),
                'FieldAtDB': True,
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00',
                '_rev': '123871283'
            },
            None,
            None,
            None,
            {
                '_id': '5',
                'ClassName': 'sl_action',
                'Explanation': 'It will be added to the updated items',
                'FieldAtDB': False,
                '_rev': '82738273',
                'CreatedAt': '2019-10-10 08:53:30.082339+00:00',
                'UpdatedAt': '2019-10-10 08:53:30.082339+00:00'
            }
        ],
        {
            'Item': {
                'saved_items': 3,
                'updated_items': 2,
                'not_saved_items': 0
            }
        },
        True
    )
]
