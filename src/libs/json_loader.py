import json

from src import env
from src.libs.config.conf import Configurations


configurations: Configurations = Configurations()


def write_json(write: dict) -> None:

    """

    Escreve um arquivo JSON a partir de um dicionário

    :param write: Dicionário a ser convertido em um arquivo JSON
    :type write: dict
    """

    file_path: str = env.JSON_FILE_PATH

    with open(file_path, 'w', encoding='utf8') as file:

        json.dump(write, file, ensure_ascii=False, indent=configurations.json_indent)


def read_json() -> dict:

    """

    Lê os informações presentes em um arquivo JSON

    :return: Um dicionário contendo as informações de um arquivo JSON
    :rtype: dict
    """

    file_path: str = env.JSON_FILE_PATH

    with open(file_path, 'r', encoding='utf8') as read:

        data: dict = json.load(read)

    return data
