import json

import os


role_list: list = [
    {
        "id": 1,
        "name": 'create_user',
        "friendly_name": 'Create User'
     },
    {
        "id": 2,
        "name": 'update_user',
        "friendly_name": 'Update User'
    },
    {
        "id": 3,
        "name": 'view_users',
        "friendly_name": 'View Users'
    }
]


def return_friendly_name(role: list) -> list:

    return_roles = []

    for iterable in role_list:

        if iterable["id"] in role:

            return_roles.append(iterable)

    return return_roles


def write_json(write: dict) -> None:

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'users.json')

    with open(file_path, 'w', encoding='utf8') as file:

        json.dump(write, file, indent=4, ensure_ascii=False)


def read_json() -> dict:

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'users.json')

    with open(file_path, 'r', encoding='utf8') as read:

        data = json.load(read)

    return data
