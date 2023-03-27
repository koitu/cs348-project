from flask import Blueprint, request
from model.Player import Player, search_players
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


@bp.route('/<player_id>/follow', methods=['POST'])
@basic_exception_handler
def add_player_to_follows(player_id: int):
    # add a player to a user's follows list
    # TODO
    pass


@bp.route('/<player_id>/follow', methods=['DELETE'])
@basic_exception_handler
def remove_player_from_follows(player_id: int):
    # remove a player from user's follows list
    # TODO
    pass


@bp.route('/<player_id>/timeline', methods=['GET'])
@basic_exception_handler
def get_player_history(player_id: int):
    # TODO
    pass


@bp.route('/<player_id>/timeline', methods=['PATCH'])
@basic_exception_handler
def modify_player_history(player_id: int):
    # TODO
    pass
