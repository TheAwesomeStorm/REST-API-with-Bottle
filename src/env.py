import os


IS_DEBUG: bool = True

DEBUG_PORT: str = '8080'

HOST: str = 'localhost'

JSON_FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'users.json')

OPERATION_PORT: str = '8888'
