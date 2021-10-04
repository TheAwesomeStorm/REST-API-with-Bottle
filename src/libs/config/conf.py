from src import env
from src.libs.singleton_metaclass import SingletonMetaclass


class Configurations(metaclass=SingletonMetaclass):  # class Configurations:

    """

    Class that defines the configuration for the program

    """

    # __instance = None

    def __init__(self, debug: bool = env.IS_DEBUG):

        self.bottle_host = env.HOST

        if debug:

            self.bottle_port = env.DEBUG_PORT

            self.json_indent = 4

        else:

            self.bottle_port = env.OPERATION_PORT

            self.json_indent = None

    # @classmethod
    # def singleton(cls):
    #
    #     if cls.__instance is None:
    #
    #         cls.__instance = cls()
    #
    #     return cls.__instance
