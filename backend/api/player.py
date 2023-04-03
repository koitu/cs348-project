from flask import Blueprint, request
from model.Player import Player, search_players, return_all_players
from model.User import User
from errors import basic_exception_handler


bp = Blueprint('player', __name__)


# GET http://127.0.0.1/api/players?name=<name>
# GET http://127.0.0.1/api/players?team_id=<team>
@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_players():
    args = request.args
    player_name = args.get("name")
    team_id = args.get("team_id")

    players = search_players(
        player_name=player_name,
        team_id=team_id,
    )
    return {'players': [player.to_dict() for player in players]}


#only user with admin id can use this
@bp.route('/all', methods=['GET'])
@basic_exception_handler
def get_all_players():
    admin_id = request.args.get("id")
    user = User(account_id=admin_id)
    if (user.is_admin()):
        players = return_all_players()
        return {'players': [player.to_dict() for player in players]}
    else:
        return {"status" : "BAD"}

@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_player():
    body = request.get_json()
    player_name = body.get('player_name')
    birthday = body.get('birthday')
    nationality = body.get('nationality')
    position = body.get('position')

    player = Player(
        player_name=player_name,
        birthday=birthday,
        nationality=nationality,
        position=position,
    )
    player.create()
    return {'status': 'OK', 'player_id': player.player_id}


@bp.route('/<player_id>', methods=['GET'])
@basic_exception_handler
def get_player(player_id: int):
    player = Player(player_id=player_id)
    player.get()
    return player.to_dict()


@bp.route('/<player_id>', methods=['PATCH'])
@basic_exception_handler
def update_player(player_id: int):
    player = Player(player_id=player_id)
    player.get()

    body = request.get_json()
    player.player_name = body.get('player_name')
    player.birthday = body.get('birthday')
    player.nationality = body.get('nationality')
    player.position = body.get('position')

    player.update()
    return {'status': 'OK'}


@bp.route('/<player_id>', methods=['DELETE'])
@basic_exception_handler
def delete_player(player_id: int):
    player = Player(player_id=player_id)
    player.delete()

    return {'status': 'OK'}

# what is this used for ? in case of large data we should not pass this to our frontend
# GET http://127.0.0.1:5000/api/players/<player_id>/followers
@bp.route('/<player_id>/followers', methods=['GET'])
@basic_exception_handler
def get_followers(player_id: int):
    player = Player(player_id=player_id)
    result = player.get_followers()

    users = [User(account_id=r[0]) for r in result]
    for u in users:
        u.get()

    return {'users': [u.to_dict() for u in users]}

# GET http://127.0.0.1:5000/api/players/<player_id>/followers
@bp.route('/<player_id>/check-follower', methods=['GET'])
@basic_exception_handler
def check_if_follower_player(player_id: int):
    player = Player(player_id=player_id)
    user_id = request.args.get("account_id")
    result = player.get_followers(user_id)

    if len(result) != 0:
        return {"status": "OK"}
    else:
        return {"status": "BAD"}
    



# TODO: may need to change method of user auth later
# http://127.0.0.1:5000/api/players/<player_id>/followers?account_id=<account_id>
@bp.route('/<player_id>/followers', methods=['POST'])
@basic_exception_handler
def add_player_to_follows(player_id: int):
    args = request.args
    account_id = args.get("account_id")

    # check that the account exists
    user = User(account_id=int(account_id))
    user.get()

    player = Player(player_id=player_id)
    # TODO: check if account is a user
    # TODO: check if accound is already following
    player.add_to_followers(account_id=account_id)

    return {'status': 'OK'}


@bp.route('/<player_id>/followers', methods=['DELETE'])
@basic_exception_handler
def remove_player_from_follows(player_id: int):
    args = request.args
    account_id = args.get("account_id")

    # check that the account exists
    user = User(account_id=account_id)
    user.get()

    team = Player(player_id=player_id)
    # TODO: check if accound is already following
    team.remove_from_followers(account_id=account_id)

    return {'status': 'OK'}


# @bp.route('/<player_id>/timeline', methods=['GET'])
# @basic_exception_handler
# def get_player_history(player_id: int):
#     # TODO
#     pass


# @bp.route('/<player_id>/timeline', methods=['PATCH'])
# @basic_exception_handler
# def modify_player_history(player_id: int):
#     # TODO
#     pass
