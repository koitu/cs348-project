from flask import Blueprint, request

bp = Blueprint('match', __name__)


@bp.route('/', methods=['GET'], strict_slashes=False)
def get_matches():
    pass


@bp.route('/', methods=['POST'], strict_slashes=False)
def add_match():
    pass


@bp.route('/<match_id>', methods=['GET'])
def get_match(match_id: int):
    pass


@bp.route('/<match_id>', methods=['PATCH'])
def modify_match(match_id: int):
    pass


@bp.route('/<match_id>', methods=['DELETE'])
def delete_match(match_id: int):
    pass


@bp.route('/<match_id>/timeline', methods=['GET'])
def get_match_timeline(match_id: int):
    pass


@bp.route('/<match_id>/timeline', methods=['PATCH'])
def modify_match_timeline(match_id: int):
    pass
