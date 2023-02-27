from functools import wraps


class BadRequest(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class NotFoundError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class MatchNotFoundError(NotFoundError):
    def __init__(self, match_id):
        super().__init__(f"match '{match_id}' could not be found")


class PlayerNotFoundError(NotFoundError):
    def __init__(self, player_id) -> None:
        super().__init__(f"player '{player_id}' could not be found")


class TeamNotFoundError(NotFoundError):
    def __init__(self, team_id):
        super().__init__(f"team '{team_id}' could not be found")


class UserNotFoundError(NotFoundError):
    def __init__(self, account_id):
        super().__init__(f"user '{account_id}' could not be found")


class AlreadyExistsError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class MatchAlreadyExistsError(AlreadyExistsError):
    def __init__(self, match_id):
        super().__init__(f"match '{match_id}' already exists in the database")


class PlayerAlreadyExistsError(AlreadyExistsError):
    def __init__(self, player_id):
        super().__init__(f"player '{player_id}' already exists in the database")


class TeamAlreadyExistsError(AlreadyExistsError):
    def __init__(self, team_id):
        super().__init__(f"team '{team_id}' already exists in the database")


class UserAlreadyExistsError(AlreadyExistsError):
    def __init__(self, user_id):
        super().__init__(f"user '{user_id}' already exists in the database")


class DatabaseConnectionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class DatabasePermissionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


# calls the function then handles some basic exceptions that may be thrown:
# - query for non-existing item
# - adding existing item
# - database connection/permission error
def basic_exception_handler(f: callable) -> callable:
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BadRequest as err:
            return {'error': str(err)}, 400
        except NotFoundError as err:
            return {'error': str(err)}, 404
        except AlreadyExistsError as err:
            return {'error': str(err)}, 409
        except DatabaseConnectionError as err:
            return {'error': str(err)}, 500
        except DatabasePermissionError as err:
            return {'error': str(err)}, 500
    return wrapper
