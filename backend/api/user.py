from flask import Blueprint, request
from model.User import User, search_users, login
from errors import basic_exception_handler


bp = Blueprint('user', __name__)


# NOT SECURE
# http://127.0.0.1:5000/api/users/login?username=<username>&password=<password>
@bp.route('/login', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def user_login():
    args = request.args
    username = args.get('username')
    password = args.get('password')

    result = login(username, password)
    if result is not None:
        return {'status': 'OK', 'id': result}
    return {'status': "BAD"}


# GET http://127.0.0.1/api/users?username=<username>
# GET http://127.0.0.1/api/users?fullname=<fullname>
@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_users():
    args = request.args
    username = args.get('username')
    fullname = args.get('fullname')

    users = search_users(
        username=username,
        fullname=fullname,
    )

    return {'users': [user.to_dict() for user in users]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_user():
    body = request.get_json()
    username = body.get('username')
    email = body.get('email')
    password = body.get('password')
    fullname = body.get('fullname')

    user = User(
        username=username,
        email=email,
        password=password,
        fullname=fullname,
        )

    user.create()
    return {'status': 'OK'}


@bp.route('/<account_id>', methods=['GET'])
@basic_exception_handler
def get_user(account_id: int):
    user = User(account_id=account_id)

    user.get()
    return user.to_dict()


@bp.route('/<account_id>', methods=['PATCH'])
@basic_exception_handler
def modify_user(account_id: int):
    user = User(account_id=account_id)
    user.get()

    body = request.get_json()
    user.username = body.get('username')
    user.email = body.get('email')
    user.password = body.get('password')
    user.fullname = body.get('fullname')

    user.update()
    return {'status': 'OK'}


@bp.route('/<account_id>', methods=['DELETE'])
@basic_exception_handler
def delete_user(account_id: int):
    user = User(account_id=account_id)

    user.delete()
    return {'status': 'OK'}


@bp.route('/<account_id>/feed', methods=['GET'])
@basic_exception_handler
def get_user_feed(account_id: int):
    # get a user's feed (like a twitter timeline)
    # TODO
    pass


@bp.route('/<account_id>/teams', methods=['GET'])
@basic_exception_handler
def get_user_teams(account_id: int):
    # TODO
    pass


@bp.route('/<account_id>/follows', methods=['GET'])
@basic_exception_handler
def get_user_follows(account_id: int):
    # TODO
    pass


@bp.route('/<account_id>/password', methods=['PATCH'])
@basic_exception_handler
def password_reset(account_id: int):
    # TODO
    pass
