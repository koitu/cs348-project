from flask import Flask
from flask_cors import CORS
import click

from mysql.connector import connect

from utils import create_database, mysql_connection


@click.command()
@click.option("--init-db",
              is_flag=True,
              help="Connects to database and creates tables")
def app(init_db):
    app = Flask(__name__)

    if init_db:
        create_database()

        print("current troubleshooting with inserting many tables\n\n")
        raise Exception()

        # note that autocommit=True
        with mysql_connection() as con:
            with con.cursor() as cursor:
                with open('db/Test.sql') as f:
                    print(f.read())

                with open('db/Test.sql') as f:
                    cursor.execute(f.read(), multi=True)

        # when fetching tables, it only finds the first table
        with mysql_connection() as con:
            with con.cursor() as cursor:
                cursor.execute("show tables;")
                result = cursor.fetchall()

                for x in result:
                    print(x)

        # with mysql_connection() as con, con.cursor() as cursor:
        #     with app.open_resource('db/Entities.sql') as f:
        #         cursor.execute(f.read().decode('utf8'),  multi=True)

        # with mysql_connection() as con, con.cursor() as cursor:
        #     with app.open_resource('db/Relationships.sql') as f:
        #         cursor.execute(f.read().decode('utf8'),  multi=True)

        # with mysql_connection() as con, con.cursor() as cursor:
        #     with app.open_resource('db/SampleData.sql') as f:
        #         cursor.execute(f.read().decode('utf8'),  multi=True)

    else:
        CORS(app)

        from api import match, player, team, user

        app.register_blueprint(match.bp, url_prefix='/api/matches')
        app.register_blueprint(player.bp, url_prefix='/api/players')
        app.register_blueprint(team.bp, url_prefix='/api/teams')
        app.register_blueprint(user.bp, url_prefix='/api/users')

        app.run()


if __name__ == "__main__":
    app()
    # to init the databases run:
    # python app.py --init-db
