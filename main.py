import json

from users_registry import UsersRegistry

from bottle import get, post, put, delete, request, response, run


users: UsersRegistry = UsersRegistry()


@get('/api/user')
def show_all_users() -> str:

    if 3 in users.show_access(int(request.get_cookie('id'))):

        return json.dumps(users.show_all_users(), ensure_ascii=False, indent=4)

    else:

        return "Acesso inválido"


@get('/api/user/<identifier:int>')
def show_user(identifier: int) -> str:

    if 3 in users.show_access(int(request.get_cookie('id'))):

        return json.dumps(users.show_user(identifier), ensure_ascii=False, indent=4)

    else:

        return "Acesso inválido"


@get('/api/user/<identifier:int>/role')
def show_user_role(identifier: int) -> str:

    if 3 in users.show_access(int(request.get_cookie('id'))):

        return json.dumps(users.show_friendly_access(identifier), ensure_ascii=False, indent=4)

    else:

        return "Acesso inválido"


@post('/api/login')
def login() -> str:

    user_id: str = request.json.get('user_id')

    user_pwd: str = request.json.get('user_pwd')

    credential: int = users.check_credentials(user_id, user_pwd)

    if credential:

        response.set_cookie("id", str(users.check_credentials(user_id, user_pwd)))

        return 'Login efetivado e cookie salvo'

    else:

        return 'Usuário ou senha incorretos'


@post('/api/user')
def create_user() -> str:

    if 1 in users.show_access(int(request.get_cookie('id'))):

        name: str = request.json.get('name')

        email: str = request.json.get('email')

        password: str = request.json.get('password')

        users.create_user(name, email, password)

        return show_all_users()

    else:

        return 'Acesso inválido'


@post('/api/user/<identifier:int>/role')
def grant_user_role(identifier: int) -> str:

    if 2 in users.show_access(int(request.get_cookie('id'))):

        role_number: int = request.json.get('role_number')

        users.grant_access(identifier, role_number)

        return show_all_users()

    else:

        return 'Acesso inválido'


@put('/api/user/<identifier:int>')
def update_user(identifier: int) -> str:

    if 2 in users.show_access(int(request.get_cookie('id'))):

        attribute: str = request.json.get('attribute')

        value: str = request.json.get('value')

        users.update_user(identifier, attribute, value)

        return show_all_users()

    else:

        return 'Acesso inválido'


@put('/api/save')
def save_changes() -> None:

    users.export_json_file()


@delete('/api/user/<identifier:int>')
def delete_user(identifier: int) -> str:

    if 1 in users.show_access(int(request.get_cookie('id'))):

        users.delete_user(identifier)

        return show_all_users()

    else:

        return 'Acesso inválido'


@delete('/api/user/<identifier:int>/role/<role_num:int>')
def revoke_user_role(identifier: int, role_num: int) -> str:

    if 2 in users.show_access(int(request.get_cookie('id'))):

        users.revoke_access(identifier, role_num)

        return show_all_users()

    else:

        return 'Acesso inválido'


run(host='localhost', port='8080', debug=True)
