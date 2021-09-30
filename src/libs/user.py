class User:

    """

    Objeto contendo uma lista com os dados de todos usuários

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

        show_dict: dict = {
            "id": self.identifier,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "roles": self.roles
        }

        return show_dict

    def grant_role(self, role_identifier: int) -> None:  # kind of set roles

        if role_identifier not in self.roles:

            self.roles.append(role_identifier)

    def revoke_role(self, role_identifier: int) -> None:

        self.roles.remove(role_identifier)

    def show_all_roles(self) -> list[int]:  # get roles

        return self.roles
