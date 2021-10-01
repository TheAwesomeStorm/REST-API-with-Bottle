from src.libs.user import User
from src.libs.roles import return_friendly_name
from src.libs.singleton import Singleton


class UsersRegistry(metaclass=Singleton):

    """

    Objeto contendo as informações de todos usuários e seus atributos

    """

    def __init__(self) -> None:

        self.all_users: dict = {}

    def create_user(self, name: str, email: str, password: str, roles: list[int] = None) -> None:

        if roles is None:

            roles = []

        new_user: User = User(name, email, password, roles)

        self.all_users[new_user.identifier] = new_user

    def delete_user(self, identifier: int) -> None:

        del self.all_users[identifier]

    def show_all_users(self) -> list:

        result: list[dict] = []

        for user in self.all_users.values():

            result.append(user.show())

        return result

    def show_user(self, identifier: int) -> dict:

        return self.all_users[identifier].show()

    def update_user(self, identifier: int, attribute: str, value: str) -> None:  # set_attributes

        setattr(self.all_users[identifier], attribute, value)

    def show_attribute(self, identifier: int, attribute: str) -> str:  # get_attributes

        return getattr(self.all_users[identifier], attribute)

    def grant_access(self, identifier: int, role_number: int) -> None:

        self.all_users[identifier].grant_role(role_number)

    def revoke_access(self, identifier: int, role_number: int) -> None:

        self.all_users[identifier].revoke_role(role_number)

    def show_access(self, identifier: int) -> list[int]:

        return self.all_users[identifier].show_all_roles()

    def show_friendly_access(self, identifier: int) -> list:

        return return_friendly_name(self.all_users[identifier].show_all_roles())
