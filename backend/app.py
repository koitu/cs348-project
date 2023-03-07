from flask import Flask
from flask_cors import CORS
import click

from utils import create_database, mysql_connection


@click.command()
@click.option("--init-db",
              is_flag=True,
              help="Connects to database and creates tables")
def app(init_db):
    app = Flask(__name__)

    if init_db:
        create_database()

        with mysql_connection() as con, con.cursor() as cursor:
            with app.open_resource('db/Entities.sql') as f:
                cursor.execute(f.read().decode('utf8'), multi=True)

        with mysql_connection() as con, con.cursor() as cursor:
            with app.open_resource('db/Relationships.sql') as f:
                cursor.execute(f.read().decode('utf8'),  multi=True)

        with mysql_connection() as con, con.cursor() as cursor:
            with app.open_resource('db/SampleData.sql') as f:
                cursor.execute(f.read().decode('utf8'),  multi=True)

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
