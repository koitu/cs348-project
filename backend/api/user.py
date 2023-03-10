from flask import Blueprint, request
from model.User import User, search_users
from errors import basic_exception_handler


bp = Blueprint('user', __name__)


@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_users():
    body = request.get_json()

    username = None

    if body:
        if 'username' in body:
            username = body['username']

    users = search_users(
        username=username,
        fuzzy=True,
    )
    # TODO: stream the response so we can have pagementation
    return {'users': [user.to_dict() for user in users]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_user():
    body = request.get_json()

    username = None
    email = None
    password = None
    fullname = None

    if body:
        if 'username' in body:
            username = body['username']
        if 'email' in body:
            email = body['email']
        if 'password' in body:
            password = body['password']
        if 'fullname' in body:
            fullname = body['fullname']

    user = User(
        username=username,
        email=email,
        password=password,
        fullname=fullname,
        )
    user.create()
    return {'status': 'OK', 'account_id': user.account_id}


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
    if body:
        if 'username' in body:
            user.username = body['username']
        if 'email' in body:
            user.email = body['email']
        if 'password' in body:
            user.password = body['password']
        if 'fullname' in body:
            user.fullname = body['fullname']

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
