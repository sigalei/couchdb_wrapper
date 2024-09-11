import os


def get_environment_variable(variable_name):
    environment_var = os.environ.get(variable_name)
    if not environment_var:
        raise AttributeError(
            f'Environment variable {variable_name} could not be found')
    return environment_var