from src.libs.singleton import Singleton
from src.libs.users_registry import UsersRegistry


class Authorization(metaclass=Singleton):

    """

    Utility class to handle the authentications and access for this Web APÌ

    """

    def __init__(self):

        self.login: bool = False

        self.create_user_access: bool = False

        self.update_user_access: bool = False

        self.view_user_access: bool = False

    def __request_access(self, user_access: list[int]):

        if 1 in user_access:

            self.create_user_access = True

        if 2 in user_access:

            self. update_user_access = True

        if 3 in user_access:

            self.view_user_access = True

    def request_login(self, user_email: str, user_password: str, users: UsersRegistry) -> int:

        for user in users.all_users.values():

            if user.email == user_email and user.password == user_password:

                self.login = True

                self.__request_access(user.show_all_roles())

                return user.identifier

            else:

                return 0
