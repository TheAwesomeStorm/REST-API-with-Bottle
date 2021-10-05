"""

Define a classe referente aos usuários da API

"""


class User:

    """

    Contém as informações de um usuário

    :param name: Nome do usuário
    :type name: str
    :param email: E-mail do usuário
    :type email: str
    :param password: Senha de acesso do usuário na API
    :type password: str
    :param roles: Lista de identificadores das permissões do usuário na API
    :type roles: list[int]
    """

    identifier_seed: int = 1

    def __init__(self, name: str, email: str, password: str, roles: list[int]) -> None:

        self.name: str = name

        self.email: str = email

        self.password: str = password

        self.roles: list[int] = roles

        self.identifier: int = self.identifier_seed

        self.__class__.identifier_seed += 1

    def show(self) -> dict:

        """

        Reúne e informa os atributos de uma instância de :class:`User`

        :return: Todos atributos deste objeto
        :rtype: dict
        """

        show_dict: dict = {
            "id": self.identifier,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "roles": self.roles
        }

        return show_dict

    def grant_role(self, role_identifier: int) -> None:

        """

        Adiciona uma permissão específica, se esta já não existe na instância

        :param role_identifier: Identificador da permissão
        :type role_identifier: int
        """

        if role_identifier not in self.roles:

            self.roles.append(role_identifier)

    def revoke_role(self, role_identifier: int) -> None:

        """

        Remove uma permissão específica

        :param role_identifier: Identificador da permissão
        :type role_identifier: int
        """

        self.roles.remove(role_identifier)
