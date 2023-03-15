from flask import Blueprint, request
from model.Match import Match, search_matches_for_team
from errors import basic_exception_handler


bp = Blueprint('match', __name__)


@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_matches():
    body = request.get_json()

    team_id = None
    other_team_id = None

    if body:
        if 'team_id' in body:
            team_id = body['team_id']
        if 'other_team_id' in body:
            other_team_id = body['other_team_id']

    matches = search_matches_for_team(
        team_id=team_id,
        fuzzy=True
    )
    # TODO: stream the response so that we can have pagementation
    return {'matches': [match.to_dict() for match in matches]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_match():
    body = request.get_json()

    team1_id = None
    team2_id = None
    team1_score = None
    team2_score = None
    date = None
    location = None

    if body:
        if 'team1_id' in body:
            team1_id = body['team1_id']
        if 'team2_id' in body:
            team2_id = body['team2_id']
        if 'team1_score' in body:
            team1_score = body['team1_score']
        if 'team2_score' in body:
            team2_score = body['team2_score']
        if 'date' in body:
            date = body['date']
        if 'location' in body:
            location = body['location']

    match = Match(
        team1_id=team1_id,
        team2_id=team2_id,
        team1_score=team1_score,
        team2_score=team2_score,
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
        if 'team1_id' in body:
            match.team1_id = body['team1_id']
        if 'team2_id' in body:
            match.team2_id = body['team2_id']
        if 'team1_score' in body:
            match.team1_score = body['team1_score']
        if 'team2_score' in body:
            match.team2_score = body['team2_score']
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
