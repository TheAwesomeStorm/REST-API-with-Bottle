from src.libs.json_loader import read_json, write_json
from src.libs.users_registry import UsersRegistry


def import_json(users: UsersRegistry) -> None:

    read_dictionary: dict = read_json()

    for item in read_dictionary['users']:

        users.create_user(item['name'], item['email'], item['password'], item['roles'])


def export_json(users: UsersRegistry) -> None:

    write_dictionary: dict = {

            "users": users.show_all_users(),

            "roles": read_json()['roles']

        }

    write_json(write_dictionary)
