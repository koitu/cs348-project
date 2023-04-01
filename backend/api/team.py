from flask import Blueprint, request
from model.Team import Team, search_teams  # search_teams_played
from model.User import User
from errors import basic_exception_handler


bp = Blueprint('team', __name__)


# GET http://127.0.0.1/api/players?name=<name>
# GET http://127.0.0.1/api/players?player_ids=<player1>,<player2>
@bp.route('/', methods=['GET'], strict_slashes=False)
@basic_exception_handler
def get_teams():
    args = request.args
    team_name = args.get("name")
    players = []

    if 'team_ids' in args:
        players = args.get('team_ids').split(",")

    teams = search_teams(
        team_name=team_name,
        players=players,
    )
    return {'teams': [team.to_dict() for team in teams]}


@bp.route('/', methods=['POST'], strict_slashes=False)
@basic_exception_handler
def create_team():
    body = request.get_json()
    abbrv = body.get('abbrv')
    team_name = body.get('team_name')
    logo_url = body.get('logo_url')
    since = body.get('since')
    location = body.get('location')

    team = Team(
        abbrv=abbrv,
        team_name=team_name,
        logo_url=logo_url,
        since=since,
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


# TODO: delete this because overlaps with GET
@bp.route('/played', methods=['GET'])
@basic_exception_handler
def get_played_teams():
    args = request.args
    players = []

    if 'player_id' in args:
        players = [args.get('player_id')]

    teams = search_teams(
        players=players,
    )
    return {'teams': [team.to_dict() for team in teams]}


@bp.route('/<team_id>', methods=['PATCH'])
@basic_exception_handler
def modify_team(team_id: int):
    team = Team(team_id=team_id)
    team.get()

    body = request.get_json()
    team.abbrv = body.get('abbrv')
    team.team_name = body.get('team_name')
    team.logo_url = body.get('logo_url')
    team.since = body.get('since')
    team.location = body.get('location')

    team.update()
    return {'status': 'OK'}


@bp.route('/<team_id>', methods=['DELETE'])
@basic_exception_handler
def delete_team(team_id: int):
    team = Team(team_id=team_id)
    team.delete()

    return {'status': 'OK'}


# GET http://127.0.0.1:5000/api/teams/<team_id>/followers
@bp.route('/<team_id>/followers', methods=['GET'])
@basic_exception_handler
def get_followers(team_id: int):
    team = Team(team_id=team_id)
    result = team.get_followers()

    users = [User(account_id=r[0]) for r in result]
    for u in users:
        u.get()

    return {'users': [u.to_dict() for u in users]}


# TODO: may need to change method of user auth later
# http://127.0.0.1:5000/api/teams/<team_id>/followers?account_id=<account_id>
@bp.route('/<team_id>/followers', methods=['POST'])
@basic_exception_handler
def add_team_to_follows(team_id: int):
    args = request.args
    account_id = args.get("account_id")

    # check that the account exists
    user = User(account_id=account_id)
    user.get()

    team = Team(team_id=team_id)
    # TODO: check if account is a user
    # TODO: check if accound is already following
    team.add_to_followers(account_id=account_id)

    return {'status': 'OK'}


# http://127.0.0.1:5000/api/teams/<team_id>/followers?account_id=<account_id>
@bp.route('/<team_id>/followers', methods=['DELETE'])
@basic_exception_handler
def remove_team_from_follows(team_id: int):
    args = request.args
    account_id = args.get("account_id")

    # check that the account exists
    user = User(account_id=account_id)
    user.get()

    team = Team(team_id=team_id)
    # TODO: check if accound is already following
    team.remove_from_followers(account_id=account_id)

    return {'status': 'OK'}


# @bp.route('/<team_id>/timeline', methods=['GET'])
# @basic_exception_handler
# def get_team_history(team_id: int):
#     # TODO
#     pass


# @bp.route('/<team_id>/timeline', methods=['DELETE'])
# @basic_exception_handler
# def modify_team_history(team_id: int):
#     # TODO
#     pass
