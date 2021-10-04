from src.libs.singleton_metaclass import SingletonMetaclass
from src.libs.users_registry import UsersRegistry


class Authorization(metaclass=SingletonMetaclass):

    def __init__(self):

        self.user_roles = []

        self.create_user_access: bool = False

        self.update_user_access: bool = False

        self.view_user_access: bool = False

    def request_login(self, user_email: str, user_password: str, users: UsersRegistry) -> int:

        for user in users.all_users.values():

            if user.email == user_email and user.password == user_password:

                self.inspect_user_roles(user.identifier, users)

                return user.identifier

        else:

            self.user_roles = []

            return 0

    def inspect_user_roles(self, identifier: int, users: UsersRegistry) -> None:

        try:

            self.user_roles = users.get_user(identifier).roles

        except KeyError:

            self.user_roles = []

            self.__request_acess()

        self.__request_acess()

    def __inspect_acess(self, acess_number: int) -> bool:

        if acess_number in self.user_roles:

            return True

        else:

            return False

    def __request_acess(self) -> None:

        self.create_user_access = self.__inspect_acess(1)

        self.update_user_access = self.__inspect_acess(2)

        self.view_user_access = self.__inspect_acess(3)
