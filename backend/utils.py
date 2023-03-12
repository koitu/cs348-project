import configparser

from contextlib import contextmanager
from mysql.connector import connect, MySQLConnection
from mysql.connector.errors import OperationalError, ProgrammingError

from errors import DatabaseConnectionError, DatabasePermissionError


config = configparser.ConfigParser()
config.read('config.ini')

db = config['database']


def create_database(force=False):
    with connect(
        user=db['user'],
        host=db['host'],
        port=db['port'],
        password=db['password'],
        autocommit=True,
    ) as con, con.cursor() as cursor:
        db_name = db['database']

        if not force:
            cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")

            result = cursor.fetchall()
            if len(result) == 1:
                print(f"Database {db_name} already exists. " +
                      "Do you want to remove it? [y/N] ", end="")
                x = input()

                if (x == "y" or x == "Y"):
                    print(f"Dropping database {db_name}: ", end="")
                    cursor.execute(f"DROP DATABASE {db_name};")
                    print("OK")

                else:
                    print(f"\nError: database {db_name} already exists")
                    exit(0)

        print(f"Creating database {db_name}: ", end="")
        cursor.execute(f"CREATE DATABASE {db_name};")
        print("OK")


@contextmanager
def mysql_connection() -> MySQLConnection:
    try:
        with connect(
            user=db['user'],
            host=db['host'],
            port=db['port'],
            password=db['password'],
            database=db['database'],
            autocommit=True,
        ) as con:
            yield con

    # unable to connect
    except OperationalError as e:
        raise DatabaseConnectionError(str(e))

    # invalid credentials, user does not exist, or invalid permissions
    except ProgrammingError as e:
        raise DatabasePermissionError(str(e))
