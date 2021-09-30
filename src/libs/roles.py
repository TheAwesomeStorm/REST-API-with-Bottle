from src.libs.JSON import read_json


role_list: list = read_json()['roles']


def return_friendly_name(role: list[int]) -> list:

    return_roles: list = []

    for iterable in role_list:

        if iterable["id"] in role:

            return_roles.append(iterable)

    return return_roles
