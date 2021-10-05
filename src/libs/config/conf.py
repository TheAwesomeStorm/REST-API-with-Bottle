from src import env
from src.libs.singleton_metaclass import SingletonMetaclass


class Configurations(metaclass=SingletonMetaclass):

    """

   Classe que define as configurações para a API

   :param debug: Define o ambiente da API, debug, i.e., desenvolvimento, ou produção
   :type debug: bool
    """

    def __init__(self, debug: bool = env.IS_DEBUG):

        self.bottle_host = env.HOST

        if debug:

            self.bottle_port = env.DEBUG_PORT

            self.json_indent = 4

        else:

            self.bottle_port = env.OPERATION_PORT

            self.json_indent = None
