from contextlib import contextmanager

from mysql.connector import connect, MySQLConnection  #, MySQLCursor
from mysql.connector.errors import OperationalError, ProgrammingError

from errors import DatabaseConnectionError, DatabasePermissionError

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db = config['database']


def create_database():
    try:
        with connect(
            user=db['user'],
            host=db['host'],
            port=db['port'],
            password=db['password'],
            autocommit=True,
        ) as con, con.cursor() as cursor:
            cursor.execute("CREATE DATABASE " + db['database'] + ";", multi= True)

    # unable to connect
    except OperationalError as e:
        raise DatabaseConnectionError(e.msg)

    # invalid credentials, user does not exist, or invalid permissions
    except ProgrammingError as e:
        raise DatabasePermissionError(e.msg)


@contextmanager
def mysql_connection() -> MySQLConnection:
    try:
        with connect(
            user=db['user'],
            host=db['host'],
            port=db['port'],
            password=db['password'],
            database=db['database'],
        ) as con:
            yield con

    # unable to connect
    except OperationalError as e:
        raise DatabaseConnectionError(e.msg)

    # invalid credentials, user does not exist, or invalid permissions
    except ProgrammingError as e:
        raise DatabasePermissionError(e.msg)

