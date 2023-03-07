from flask import Blueprint, request
from model.Player import Player, search_players
from errors import basic_exception_handler


bp = Blueprint('player', __name__)


@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_players():
    body = request.get_json()

    player_name = None

    if body:
        if 'player_name' in body:
            player_name = body['player_name']

    players = search_players(
        player_name=player_name,
        fuzzy=True
    )
    # TODO: stream the response so we can have pagementation
    return {'players': [player.to_dict() for player in players]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_player():
    body = request.get_json()

    player_name = None
    birthday = None
    nationality = None
    position = None

    if body:
        if 'player_name' in body:
            player_name = body['player_name']
        if 'birthday' in body:
            birthday = body['birthday']
        if 'nationality' in body:
            nationality = body['nationality']
        if 'position' in body:
            position = body['position']

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
    # TODO: at the moment I have no idea if we are going to convert strings to integer or not
    player = Player(player_id=player_id)
    player.get()
    return player.to_dict()


@bp.route('/<player_id>', methods=['PATCH'])
@basic_exception_handler
def update_player(player_id: int):
    player = Player(player_id=player_id)
    player.get()

    body = request.get_json()
    if body:
        if 'player_name' in body:
            player.player_name = body['player_name']
        if 'birthday' in body:
            player.birthday = body['birthday']
        if 'nationality' in body:
            player.nationality = body['nationality']
        if 'position' in body:
            player.position = body['position']

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
