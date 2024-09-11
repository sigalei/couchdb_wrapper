def assert_exception_msg(exception, expected_message):
    exception_message = get_exception_msg(exception)
    is_equal = exception_message == expected_message
    if not is_equal:
        print(f'Exception Message: {exception_message}')
        print(f'Expected Message: {expected_message}')
    assert is_equal


def get_exception_msg(exception):
    return str(exception.value)