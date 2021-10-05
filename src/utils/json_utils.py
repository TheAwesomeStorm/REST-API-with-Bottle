from src.libs.json_loader import read_json, write_json
from src.libs.users_registry import UsersRegistry


def import_json() -> UsersRegistry:

    """

    Transfere todas as informações de usuários em um arquivo JSON para um objeto :class:`UsersRegistry`

    :return: Um objeto contendo todas as informações de usuários presentes em um arquivo JSON
    :rtype: UsersRegistry
    """

    users: UsersRegistry = UsersRegistry()

    read_dictionary: dict = read_json()

    for item in read_dictionary['users']:

        users.create_user(item['name'], item['email'], item['password'], item['roles'])

    return users


def export_json(users: UsersRegistry) -> None:

    """

    Converte todos as informações em uma instância de :class:`UsersRegistry` para um arquivo JSON

    :param users: Objeto contendo as informações de todos os usuários
    :type users: UsersRegistry
    """

    write_dictionary: dict = {

            "users": users.show_all_users(),

            "roles": read_json()['roles']

        }

    write_json(write_dictionary)
