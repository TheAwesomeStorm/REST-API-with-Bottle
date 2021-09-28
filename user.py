class User:

    """

    Objeto contendo uma lista com os dados de todos usuários

    """

    identifier_seed = int(1)

    def __init__(self, name: str, email: str, password: str, roles: list) -> None:

        self.name = name

        self.email = email

        self.password = password

        self.roles = roles

        self.identifier = self.identifier_seed

        self.__class__.identifier_seed += 1

    def show(self) -> dict:

        show_dict = {
            "id": self.identifier,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "roles": self.roles
        }

        return show_dict

    def grant_role(self, role_identifier: int) -> None:  # setter?

        if role_identifier not in self.roles:

            self.roles.append(role_identifier)

    def revoke_role(self, role_identifier: int) -> None:

        self.roles.remove(role_identifier)

    def show_all_roles(self) -> list:  # get roles

        return self.roles
