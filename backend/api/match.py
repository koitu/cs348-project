from flask import Blueprint, request
from model.Match import Match, search_matches_for_team
from errors import basic_exception_handler


bp = Blueprint('match', __name__)

# TODO update with modified SQL relations

@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_matches():
    body = request.get_json()

    teams = []
    players = []

    if body:
        if 'teams' in body:
            teams = body['teams']
        if 'players' in body:
            players = body['players']

    matches = search_matches(
        teams=teams,
        players=players,
    )
    return {'matches': [match.to_dict() for match in matches]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_match():
    body = request.get_json()

    team_home_id = None
    team_away_id = None
    team_home_score = None
    team_away_score = None
    date = None
    location = None

    if body:
        if 'team_home_id' in body:
            team_home_id = body['team_home_id']
        if 'team_away_id' in body:
            team_away_id = body['team_away_id']
        if 'team_home_score' in body:
            team_home_score = body['team_home_score']
        if 'team_away_score' in body:
            team_away_score = body['team_away_score']
        if 'date' in body:
            date = body['date']
        if 'location' in body:
            location = body['location']

    match = Match(
        team_home_id=team_home_id,
        team_away_id=team_away_id,
        team_home_score=team_home_score,
        team_away_score=team_away_score,
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
    if body:
        if 'team_home_id' in body:
            match.team_home_id = body['team_home_id']
        if 'team_away_id' in body:
            match.team_away_id = body['team_away_id']
        if 'team_home_score' in body:
            match.team_home_score = body['team_home_score']
        if 'team_away_score' in body:
            match.team_away_score = body['team_away_score']
        if 'date' in body:
            match.date = body['date']
        if 'location' in body:
            match.location = body['location']

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
