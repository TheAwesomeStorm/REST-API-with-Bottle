from src.libs.user import User
from src.libs.roles import return_friendly_name
from src.libs.singleton_metaclass import SingletonMetaclass


class UsersRegistry(metaclass=SingletonMetaclass):

    """

    Define uma classe como base de dados para todos os usuários, estes objetos de :class:`User`

    """

    def __init__(self) -> None:

        self.all_users: dict = {}

    def create_user(self, name: str, email: str, password: str, roles: list[int] = None) -> None:

        """

        Cadastrar um usuário

        :param name: Nome do usuário
        :type name: str
        :param email: E-mail do usuário
        :type email: str
        :param password: Senha de acesso do usuário
        :type password: str
        :param roles: Identificadores das permissões do usuário na API
        :type roles: list[int]
        """

        if roles is None:

            roles = []

        new_user: User = User(name, email, password, roles)

        self.all_users[new_user.identifier] = new_user

    def delete_user(self, identifier: int) -> None:

        """

        Excluir um usuário específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int
        """

        del self.all_users[identifier]

    def show_all_users(self) -> list[dict]:

        """

        Visualizar todos os usuários cadastrados

        :return: Uma lista com todos os usuários e seus atributos
        :rtype: list[dict]
        """

        result: list[dict] = []

        for user in self.all_users.values():

            result.append(user.show())

        return result

    def show_user(self, identifier: int) -> dict:

        """

        Visualizar um usuário específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int

        :return: Um dicionário com os atributos de um usuário específico
        :rtype: dict
        """

        return self.all_users[identifier].show()

    def get_user(self, identifier: int) -> User:

        """

        Visualiza a instância de um objeto :class:`User` específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int

        :return: A instância do objeto
        :rtype: User
        """

        return self.all_users[identifier]

    def set_attribute(self, identifier: int, attribute: str, value: str) -> None:

        """

        Atualizar as informações de um usuário específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int
        :param attribute: Nome do atributo, e.g., name
        :type attribute: str
        :param value: Valor de atualização
        :type value: str
        """

        setattr(self.all_users[identifier], attribute, value)

    def get_attribute(self, identifier: int, attribute: str) -> str:

        """

        Visualizar o atributo de um usuário específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int
        :param attribute: Nome do atributo, e.g., name
        :type attribute: str

        :return: Valor do atributo
        :rtype: str
        """

        return getattr(self.all_users[identifier], attribute)

    def grant_access(self, identifier: int, role_number: int) -> None:

        """

        Adicionar uma permissão a um usuário específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int
        :param role_number: Identificador da permissão
        :type role_number: int
        """

        self.all_users[identifier].grant_role(role_number)

    def revoke_access(self, identifier: int, role_number: int) -> None:

        """

        Excluir uma permissão de um usuário específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int
        :param role_number: Identificador da permissão
        :type role_number: int
        """

        self.all_users[identifier].revoke_role(role_number)

    def get_roles(self, identifier: int) -> list[int]:

        """

        Visualizar todas as permissões de um usuário específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int

        :return: Lista de identificadores das permissões do usuários
        :rtype: list[int]
        """

        return self.all_users[identifier].roles

    def show_friendly_access(self, identifier: int) -> list:

        """

        Visualizar as descrições de todas as permissões de um usuário específico

        :param identifier: Identificador do usuário na base de dados
        :type identifier: int

        :return: Descrições das permissões do usuário
        :rtype: list
        """

        return return_friendly_name(self.all_users[identifier].roles)
