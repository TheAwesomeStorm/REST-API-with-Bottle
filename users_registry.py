from roles import return_friendly_name

from roles import write_json

from roles import read_json

from roles import role_list

from user import User


class UsersRegistry:

    """

    Objeto contendo as informações de todos usuários e seus atributos

    """

    def __init__(self) -> None:

        self.list_of_users = []

        self.import_json_file()

    def create_user(self, name: str, email: str, password: str, roles: list = None) -> None:

        if roles is None:

            roles = []

        print('Cadastrar um novo usuário')

        new_user = User(name, email, password, roles)

        self.list_of_users.append(new_user)

    def delete_user(self, identifier: int) -> None:

        print('Excluir um usuário específico')

        self.list_of_users.remove(self.return_user(identifier))

    def return_user(self, identifier: int) -> User:  # tornar privado

        # make one and only one of two arguments necessary

        for item in self.list_of_users:

            if item.identifier == identifier:

                return item

    def show_all_users(self) -> list:

        print('Visualizar todos os usuários cadastrados')

        result = []

        for item in self.list_of_users:

            result.append(item.show())

        return result

    def show_user(self, identifier: int) -> dict:

        print('Visualizar um usuário específico')

        return self.return_user(identifier).show()

    def update_user(self, identifier: int, attribute: str, value: str) -> None:  # set_attributes

        print('Atualizar um usuário específico')

        setattr(self.return_user(identifier), attribute, value)

    def show_attribute(self, identifier: int, attribute: str) -> str:  # get_attributes

        print('Visualizar um atributo específico: {}'.format(attribute))

        return getattr(self.return_user(identifier), attribute)

    def grant_access(self, identifier: int, role_number: int) -> None:

        print('Adicionar uma permissão a um usuário específico')

        self.return_user(identifier).grant_role(role_number)

    def revoke_access(self, identifier: int, role_number: int) -> None:

        print('Excluir uma permissão de um usuário específico')

        self.return_user(identifier).revoke_role(role_number)

    def show_access(self, identifier: int) -> list:

        print('Visualizar todas as permissões de um usuário específico')

        return self.return_user(identifier).show_all_roles()

    def show_friendly_access(self, identifier: int) -> list:

        print('Visualizar, de forma amigável, todas as permissões de um usuário específico')

        return return_friendly_name(self.return_user(identifier).show_all_roles())

    def export_json_file(self) -> None:

        write_dictionary = {

            "users": self.show_all_users(),

            "roles": role_list

        }

        write_json(write_dictionary)

        print("Arquivo JSON exportado")

    def import_json_file(self) -> None:

        read_dictionary = read_json()

        for item in read_dictionary['users']:

            self.create_user(item['name'], item['email'], item['password'], item['roles'])

    def check_credentials(self, user_email: str, password: str) -> int:

        identifier: int = 0

        for user in self.list_of_users:

            if user.email == user_email and user.password == password:

                identifier = user.identifier

        return identifier
