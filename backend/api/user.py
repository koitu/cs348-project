from flask import Blueprint, request
from model.User import User

bp = Blueprint('user', __name__)


@bp.route('/', methods=['GET'], strict_slashes=False)
def get_users():
    # body = request.get_json()
    pass


@bp.route('/', methods=['POST'], strict_slashes=False)
def create_user():
    # body = request.get_json()
    pass


@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id: int):
    user = User(user_id)
    user.get()
    return user.to_dict()


@bp.route('/<user_id>', methods=['PATCH'])
def modify_user(user_id: int):
    body = request.get_json()  # a dict
    user = User(user_id)
    user.get()

    # something

    user.update()
    return {'status': 'OK'}


@bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    pass


# get a user's feed (like a twitter timeline)
@bp.route('/<user_id>/feed', methods=['GET'])
def get_user_feed(user_id: int):
    pass


@bp.route('/<user_id>/teams', methods=['GET'])
def get_user_teams(user_id: int):
    pass


@bp.route('/<user_id>/follows', methods=['GET'])
def get_user_follows(user_id: int):
    pass


@bp.route('/<user_id>/password', methods=['PATCH'])
def password_reset(user_id: int):
    pass
