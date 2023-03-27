from functools import wraps

from mysql.connector import (
    ProgrammingError,
    OperationalError,
    DatabaseError,
)


class BadRequest(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class NotFoundError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class MatchNotFoundError(NotFoundError):
    def __init__(self, match_id):
        super().__init__(
            f"Match with ID {match_id} could not be found")


class PlayerNotFoundError(NotFoundError):
    def __init__(self, player_id) -> None:
        super().__init__(
            f"Player with ID {player_id} could not be found")


class TeamNotFoundError(NotFoundError):
    def __init__(self, team_id):
        super().__init__(
            f"Team with ID {team_id} could not be found")


class UserNotFoundError(NotFoundError):
    def __init__(self, account_id):
        super().__init__(
            f"User with ID {account_id} could not be found")


class AlreadyExistsError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class MatchExistsError(AlreadyExistsError):
    def __init__(self, match_id):
        super().__init__(
            f"Match ID {match_id} already exists in the database")


class PlayerExistsError(AlreadyExistsError):
    def __init__(self, player_id):
        super().__init__(
            f"Player ID {player_id} already exists in the database")


class TeamExistsError(AlreadyExistsError):
    def __init__(self, team_id):
        super().__init__(
            f"Team ID {team_id} already exists in the database")


class UserExistsError(AlreadyExistsError):
    def __init__(self, account_id):
        super().__init__(
            f"Account ID {account_id} already exists in the database")


class UsernameExistsError(AlreadyExistsError):
    def __init__(self, username):
        super().__init__(
            f"Username {username} is already taken")


class EmailExistsError(AlreadyExistsError):
    def __init__(self, email):
        super().__init__(
            f"Email {email} is already taken")


# Calls the function then handles some basic exceptions that may be thrown:
# - query for non-existing item
# - adding existing item
# - database connection/permission error
def basic_exception_handler(f: callable) -> callable:
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)

        # Backend errors
        except BadRequest as err:
            return {'error': str(err)}, 400
        except NotFoundError as err:
            return {'error': str(err)}, 404
        except AlreadyExistsError as err:
            return {'error': str(err)}, 409

        # Internal errors
        # note: type errors should be handled by frontend
        except ProgrammingError as err:
            # covers sql syntax, constraint checking, types,
            # database connection, permissions and more.
            return {'error': str(err)}, 500
        except OperationalError as err:
            # covers a couple of database connection problem
            return {'error': str(err)}, 500
        except DatabaseError as err:
            # covers ProgrammingError and OpertionalError and more
            return {'error': str(err)}, 500
    return wrapper
