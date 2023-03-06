from contextlib import contextmanager

from mysql.connector import connect, MySQLConnection  #, MySQLCursor
from mysql.connector.errors import OperationalError, ProgrammingError

from errors import DatabaseConnectionError, DatabasePermissionError


@contextmanager
def mysql_connection() -> MySQLConnection:
    try:
        with connect(
            host="localhost",
            port="3306",
            user="root",
            password="AStrongPassword123!",
            database="cs348",
            autocommit=True,
        ) as con:
            yield con

    # unable to connect
    except OperationalError:
        raise DatabaseConnectionError()

    # invalid credentials, user does not exist, or invalid permissions
    except ProgrammingError:
        raise DatabasePermissionError()
