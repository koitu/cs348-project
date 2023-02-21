from flask import Blueprint, request

bp = Blueprint('team', __name__)


@bp.route('/', methods=['GET'], strict_slashes=False)
def get_teams():
    pass


@bp.route('/', methods=['POST'], strict_slashes=False)
def add_team():
    pass


@bp.route('/<team_id>', methods=['GET'])
def get_team(team_id: int):
    pass


@bp.route('/<team_id>', methods=['PATCH'])
def modify_team(team_id: int):
    pass


@bp.route('/<team_id>', methods=['DELETE'])
def delete_team(team_id: int):
    pass


@bp.route('/<team_id>/follow', methods=['POST'])
def add_team_to_follows(team_id: int):
    pass


@bp.route('/<team_id>/follow', methods=['DELETE'])
def remove_team_from_follows(team_id: int):
    pass


@bp.route('/<team_id>/timeline', methods=['GET'])
def get_team_history(team_id: int):
    pass


@bp.route('/<team_id>/timeline', methods=['DELETE'])
def modify_team_history(team_id: int):
    pass
