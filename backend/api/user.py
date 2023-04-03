from flask import Blueprint, request
from model.User import User, search_users, login, return_all_users
from model.Player import Player
from model.Team import Team
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

#only user with admin id can use this
@bp.route('/all', methods=['GET'])
@basic_exception_handler
def get_all_user():
    admin_id = request.args.get("id")
    user = User(account_id=admin_id)
    if (user.is_admin()):
        users =  return_all_users()
        return {'users': [user.to_dict() for user in users]}
    else:
        return {"status" : "NOT-ADMIN"}

@bp.route('/<account_id>', methods=['GET'])
@basic_exception_handler
def get_user(account_id: int):
    user = User(account_id=account_id)

    user.get()
    return user.to_dict()

@bp.route('/<account_id>/promote', methods=['GET'])
@basic_exception_handler
def promote_user(account_id: int):
    user = User(account_id=account_id)
    user.get()
    user.promote_to_admin()
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


# http://127.0.0.1:5000/api/users/<account_id>/players
@bp.route('/<account_id>/players', methods=['GET'])
@basic_exception_handler
def get_players_followed(account_id: int):
    user = User(account_id=account_id)
    result = user.get_players_followed()

    players = [Player(player_id=r[0]) for r in result]
    for p in players:
        p.get()

    return {'players': [p.to_dict() for p in players]}

@bp.route('/<account_id>/players', methods=['DELETE'])
@basic_exception_handler
def delete_players_followed(account_id: int):
    user = User(account_id=account_id)
    body = request.get_json()
    player_id = body.get('player_id')
    user.remove_players_followed(player_id=player_id)
    return {"status" : "OK"}


# http://127.0.0.1:5000/api/users/<account_id>/teams
@bp.route('/<account_id>/teams', methods=['GET'])
@basic_exception_handler
def get_teams_followed(account_id: int):
    user = User(account_id=account_id)
    result = user.get_teams_followed()

    teams = [Team(team_id=r[0]) for r in result]
    for t in teams:
        t.get()

    return {'teams': [t.to_dict() for t in teams]}


@bp.route('/<account_id>/teams', methods=['DELETE'])
@basic_exception_handler
def delete_teams_followed(account_id: int):
    user = User(account_id=account_id)
    body = request.get_json()
    team_id = body.get('team_id')
    user.remove_team_followed(team_id=team_id)
    return {"status" : "OK"}



# @bp.route('/<account_id>/feed', methods=['GET'])
# @basic_exception_handler
# def get_user_feed(account_id: int):
#     # get a user's feed (like a twitter timeline)
#     # TODO
#     pass
