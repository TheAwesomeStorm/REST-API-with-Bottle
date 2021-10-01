from src import environment
from src.libs.singleton import Singleton


class Configurations(metaclass=Singleton):

    """

    Class that defines the configuration for the program

    """

    __instance = None

    def __init__(self, debug: bool = environment.IS_DEBUG):

        self.bottle_host = environment.HOST

        if debug:

            self.bottle_port = environment.DEBUG_PORT

            self.json_indent = 4

        else:

            self.bottle_port = environment.OPERATION_PORT

            self.json_indent = None
