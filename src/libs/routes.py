from bottle import get, post, put, delete, request, response, run
import json

from src import environment
from src.libs.config.config import Configurations
from src.libs.users_registry import UsersRegistry
from src.utils.authorization import Authorization
from src.utils.JSON_utils import import_json, export_json


authorization: Authorization = Authorization()

configurations: Configurations = Configurations()

users: UsersRegistry = UsersRegistry()

import_json(users)


@get('/api/user')
def show_all_users() -> str:

    if authorization.view_user_access:

        return json.dumps(users.show_all_users(), ensure_ascii=False, indent=configurations.json_indent)

    else:

        return 'Acesso inválido'


@get('/api/user/<identifier:int>')
def show_user(identifier: int) -> str:

    if authorization.view_user_access:

        return json.dumps(users.show_user(identifier), ensure_ascii=False, indent=configurations.json_indent)

    else:

        return 'Acesso inválido'


@get('/api/user/<identifier:int>/role')
def show_user_role(identifier: int) -> str:

    if authorization.view_user_access:

        return json.dumps(users.show_friendly_access(identifier), ensure_ascii=False, indent=configurations.json_indent)

    else:

        return 'Acesso inválido'


@post('/api/login')
def login() -> str:

    user_email: str = request.json.get('user_email')

    user_password: str = request.json.get('user_password')

    user_identifier = authorization.request_login(user_email, user_password, users)

    if authorization.login:

        response.set_cookie("id", str(user_identifier))

        return 'Login efetivado e cookie salvo'

    else:

        return 'Usuário ou senha incorretos'


@post('/api/user')
def create_user() -> str:

    if authorization.create_user_access:

        name: str = request.json.get('name')

        email: str = request.json.get('email')

        password: str = request.json.get('password')

        users.create_user(name, email, password)

        return show_process_result()

    else:

        return 'Acesso inválido'


@post('/api/user/<identifier:int>/role')
def grant_user_role(identifier: int) -> str:

    if authorization.update_user_access:

        role_number: int = request.json.get('role_number')

        users.grant_access(identifier, role_number)

        return show_process_result()

    else:

        return 'Acesso inválido'


@put('/api/user/<identifier:int>')
def update_user(identifier: int) -> str:

    if authorization.update_user_access:

        attribute: str = request.json.get('attribute')

        value: str = request.json.get('value')

        users.update_user(identifier, attribute, value)

        return show_process_result()

    else:

        return 'Acesso inválido'


@put('/api/save')
def save_changes() -> None:

    export_json(users)


@delete('/api/user/<identifier:int>')
def delete_user(identifier: int) -> str:

    if authorization.create_user_access:

        users.delete_user(identifier)

        return show_process_result()

    else:

        return 'Acesso inválido'


@delete('/api/user/<identifier:int>/role/<role_num:int>')
def revoke_user_role(identifier: int, role_num: int) -> str:

    if authorization.update_user_access:

        users.revoke_access(identifier, role_num)

        return show_process_result()

    else:

        return 'Acesso inválido'


def show_process_result() -> str:

    if environment.IS_DEBUG:

        return show_all_users()

    else:

        return 'Processo concluído'


def run_web_api(host: str = configurations.bottle_host,
                port: str = configurations.bottle_port,
                debug: bool = environment.IS_DEBUG):

    run(host=host, port=port, debug=debug)
