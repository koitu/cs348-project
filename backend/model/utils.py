from contextlib import contextmanager

from mysql.connector import connect, MySQLConnection, MySQLCursor
from mysql.connector.errors import OperationalError, ProgrammingError

from errors import DatabaseConnectionError, DatabasePermissionError

host = None
user = None
password = None


def mysql_connection() -> MySQLConnection:
    try:
        with connect(
            host=host,
            user=user,
            password=password,
        ) as con:
            return con

    # unable to connect
    except OperationalError:
        raise DatabaseConnectionError()

    # invalid credentials, user does not exist, or invalid permissions
    except ProgrammingError:
        raise DatabasePermissionError()
