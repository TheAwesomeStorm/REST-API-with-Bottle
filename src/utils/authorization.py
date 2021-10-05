from src.libs.singleton_metaclass import SingletonMetaclass
from src.libs.users_registry import UsersRegistry


class Authorization(metaclass=SingletonMetaclass):

    """

    Define as permissões do usuário após o login

    """

    def __init__(self):

        self.user_roles = []

        self.create_user_access: bool = False

        self.update_user_access: bool = False

        self.view_user_access: bool = False

    def request_login(self, user_email: str, user_password: str, users: UsersRegistry) -> int:

        """

        Procura na base de dados por um par e-mail e senha correspondentes, se encontrado realiza o login

        :param user_email: E-mail do usuário na API
        :type user_email: str
        :param user_password: Senha do usuário na API
        :type user_password: str
        :param users: Base de dados contendo todos usuários
        :type users: UsersRegistry

        :return: O identificador do usuário se o login for bem sucedido ou 0 se não
        :rtype: int
        """

        for user in users.all_users.values():

            if user.email == user_email and user.password == user_password:

                self.inspect_user_roles(user.identifier, users)

                return user.identifier

        else:

            self.user_roles = []

            return 0

    def inspect_user_roles(self, identifier: int, users: UsersRegistry) -> None:

        """

        Busca as permissões do usuário na base de dados e as armazena na classe

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int
        :param users: Base de dados contendo todos os usuários
        :type users: UsersRegistry
        """

        try:

            self.user_roles = users.get_user(identifier).roles

        except KeyError:

            self.user_roles = []

        self.__request_acess()

    def __inspect_acess(self, acess_number: int) -> bool:

        """

        Atribui se um acesso específico foi encontrado nas permissões do usuário

        :param acess_number: Identificador do acesso
        :type acess_number: int

        :return: Se o acesso foi encontrado nas permissões do usuário
        :rtype: bool
        """

        if acess_number in self.user_roles:

            return True

        else:

            return False

    def __request_acess(self) -> None:

        """

        Armazena na classe o *status* de todas as permissões do usuário

        """

        self.create_user_access = self.__inspect_acess(1)

        self.update_user_access = self.__inspect_acess(2)

        self.view_user_access = self.__inspect_acess(3)
