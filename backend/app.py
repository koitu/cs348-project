import click

from flask import Flask
from flask_cors import CORS

from utils import create_database, mysql_connection


entities = [
    "Account",
    "User",
    "Admin",
    "Player",
    "Team",
    "Game",
]

relationships = [
    "PT",
    "PG",
    "Fav_Players",
    "Fav_Teams",
]

data = [
    "player",
    "team",
    "game",
    "account",
    "user",
]


@click.command()
@click.option("--init-db",
              is_flag=True,
              help="Connects to database and creates tables")
def app(init_db):
    app = Flask(__name__)

    if init_db:
        create_database()

        with mysql_connection() as con:
            with con.cursor() as cursor:

                print("\nEntity tables:")
                for e in entities:
                    print(f"Creating table {e}: ", end="")
                    with open(f"db/entities/{e}.sql") as f:
                        cursor.execute(f.read())
                    print("OK")

                print("\nRelationship tables:")
                for r in relationships:
                    print(f"Creating table {r}: ", end="")
                    with open(f"db/relationships/{r}.sql") as f:
                        cursor.execute(f.read())
                    print("OK")

                print("\nSample data: ", end="")
                with open("db/SampleData.sql") as f:
                    for d in f.read().split("-- SPLIT --"):
                        print(d)
                        cursor.execute(d)
                print("OK")

                # print("\nProduction data:")
                # for d in data:
                #     print(f"Inserting {d} data: ", end="")
                #     with open(f"db/data/{d}.sql") as f:
                #         cursor.execute(f.read())
                #     print("OK")

        # # to double check that all tables were inserted
        # with mysql_connection() as con:
        #     with con.cursor() as cursor:
        #         cursor.execute("show tables;")
        #         result = cursor.fetchall()

        #         print("\nTables inserted:")
        #         for x in result:
        #             print(x[0])

    else:
        CORS(app)

        from api import match, player, team, user

        app.register_blueprint(match.bp, url_prefix='/api/matches')
        app.register_blueprint(player.bp, url_prefix='/api/players')
        app.register_blueprint(team.bp, url_prefix='/api/teams')
        app.register_blueprint(user.bp, url_prefix='/api/users')

        app.run()


if __name__ == "__main__":
    # to init the databases run:
    # python app.py --init-db
    app()
    # add versbose (backend command result)
    # add double verbose (the exact command the backend is running)
