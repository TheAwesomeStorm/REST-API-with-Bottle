from src.libs.json_loader import read_json


def return_friendly_name(role: list[int]) -> list:

    """

    Traduz uma lista de identificadores de permissão em suas respectivas descrições

    :param role: Lista com os identificadores de permissão
    :type role: list[int]

    :return: Uma lista com as descrições
    :rtype: list
    """

    role_list: list = read_json()['roles']

    return_roles: list = []

    for iterable in role_list:

        if iterable["id"] in role:

            return_roles.append(iterable)

    return return_roles
