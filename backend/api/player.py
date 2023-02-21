from flask import Blueprint, request

bp = Blueprint('player', __name__)


@bp.route('/', methods=['GET'], strict_slashes=False)
def get_players():
    # body = request.get_json()

    pass


@bp.route('/', methods=['POST'], strict_slashes=False)
def add_player():
    # body = request.get_json()

    pass


@bp.route('/<player_id>', methods=['GET'])
def get_player(player_id: int):
    pass


@bp.route('/<player_id>', methods=['PATCH'])
def update_player(player_id: int):
    pass


@bp.route('/<player_id>', methods=['DELETE'])
def delete_player(player_id: int):
    pass


@bp.route('/<player_id>/follow', methods=['POST'])
def add_player_to_follows(player_id: int):
    # add a player to a user's follows list
    pass


@bp.route('/<player_id>/follow', methods=['DELETE'])
def remove_player_from_follows(player_id: int):
    # remove a player from user's follows list
    pass


@bp.route('/<player_id>/timeline', methods=['GET'])
def get_player_history(player_id: int):
    pass


@bp.route('/<player_id>/timeline', methods=['PATCH'])
def modify_player_history(player_id: int):
    pass
