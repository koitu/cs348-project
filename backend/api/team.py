from flask import Blueprint, request
from model.Team import Team, search_teams
from errors import basic_exception_handler


bp = Blueprint('team', __name__)


@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_teams():
    body = request.get_json()

    team_name = None

    if body:
        if 'team_name' in request:
            team_name = body['team_name']

    teams = search_teams(
        team_name=team_name,
        fuzzy=True,
    )
    # TODO: stream the response so we can have pagementation
    return {'teams': [team.to_dict() for team in teams]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_team():
    body = request.get_json()

    team_name = None
    start_date = None
    league = None
    location = None

    if body:
        if 'team_name' in body:
            team_name = body['team_name']
        if 'start_date' in body:
            start_date = body['start_date']
        if 'league' in body:
            league = body['league']
        if 'location' in body:
            location = body['location']

    team = Team(
        team_name=team_name,
        start_date=start_date,
        league=league,
        location=location,
    )
    team.create()
    return {'status': 'OK', 'team_id': team.team_id}


@bp.route('/<team_id>', methods=['GET'])
@basic_exception_handler
def get_team(team_id: int):
    team = Team(team_id=team_id)
    team.get()
    return team.to_dict()


@bp.route('/<team_id>', methods=['PATCH'])
@basic_exception_handler
def modify_team(team_id: int):
    team = Team(team_id=team_id)
    team.get()

    body = request.get_json()
    if body:
        if 'team_name' in body:
            team.team_name = body['team_name']
        if 'start_date' in body:
            team.start_date = body['start_date']
        if 'league' in body:
            team.league = body['league']
        if 'location' in body:
            team.location = body['location']

    team.update()
    return {'status': 'OK'}


@bp.route('/<team_id>', methods=['DELETE'])
@basic_exception_handler
def delete_team(team_id: int):
    team = Team(team_id=team_id)
    team.delete()

    return {'status': 'OK'}


@bp.route('/<team_id>/follow', methods=['POST'])
@basic_exception_handler
def add_team_to_follows(team_id: int):
    # TODO
    pass


@bp.route('/<team_id>/follow', methods=['DELETE'])
@basic_exception_handler
def remove_team_from_follows(team_id: int):
    # TODO
    pass


@bp.route('/<team_id>/timeline', methods=['GET'])
@basic_exception_handler
def get_team_history(team_id: int):
    # TODO
    pass


@bp.route('/<team_id>/timeline', methods=['DELETE'])
@basic_exception_handler
def modify_team_history(team_id: int):
    # TODO
    pass
