from flask import Blueprint, request
from model.Match import Match, search_matches
from errors import basic_exception_handler


bp = Blueprint('match', __name__)


# http://127.0.0.1:5000/api/matches?team_ids=<team1>
# http://127.0.0.1:5000/api/matches?team_ids=<team1>,<team2>&player_ids=<player1>,<player2>,<player3>
@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_matches():
    teams = []
    players = []

    args = request.args
    if 'team_ids' in args:
        teams = args.get('team_ids').split(",")
    if 'player_ids' in args:
        players = args.get('player_ids').split(",")

    matches = search_matches(
        teams=teams,
        players=players,
    )
    return {'matches': [match.to_dict() for match in matches]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_match():
    body = request.get_json()
    team_home_id = body.get('team_home_id')
    team_away_id = body.get('team_away_id')
    team_home_score = body.get('team_home_score')
    team_away_score = body.get('team_away_score')
    season = body.get('season')
    date = body.get('date')
    location = body.get('location')

    match = Match(
        team_home_id=team_home_id,
        team_away_id=team_away_id,
        team_home_score=team_home_score,
        team_away_score=team_away_score,
        season=season,
        date=date,
        location=location,
    )
    match.create()
    return {'status': 'OK', 'match_id': match.match_id}


@bp.route('/<match_id>', methods=['GET'])
@basic_exception_handler
def get_match(match_id: int):
    match = Match(match_id=match_id)
    match.get()
    return match.to_dict()


@bp.route('/<match_id>', methods=['PATCH'])
@basic_exception_handler
def modify_match(match_id: int):
    match = Match(match_id=match_id)
    match.get()

    body = request.get_json()
    match.team_home_id = body.get('team_home_id')
    match.team_away_id = body.get('team_away_id')
    match.team_home_score = body.get('team_home_score')
    match.team_away_score = body.get('team_away_score')
    match.season = body.get('season')
    match.date = body.get('date')
    match.location = body.get('location')

    match.update()
    return {'status': 'OK'}


@bp.route('/<match_id>', methods=['DELETE'])
@basic_exception_handler
def delete_match(match_id: int):
    match = Match(match_id=match_id)
    match.delete()

    return {'status': 'OK'}


@bp.route('/<match_id>/timeline', methods=['GET'])
@basic_exception_handler
def get_match_timeline(match_id: int):
    # TODO
    pass


@bp.route('/<match_id>/timeline', methods=['PATCH'])
@basic_exception_handler
def modify_match_timeline(match_id: int):
    # TODO
    pass
