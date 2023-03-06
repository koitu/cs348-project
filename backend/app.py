from flask import Flask
from flask_cors import CORS
from mysql.connector import connect

import click


@click.command()
@click.option("--init-db",
              is_flag=True,
              help="Connects to database and creates tables")
def app(init_db):
    if init_db:
        with connect(
            host="localhost",
            port="3306",
            user="root",
            password="AStrongPassword123!",
            database="cs348",
            autocommit=True,
        ) as con, con.cursor() as cursor:
            app = Flask(__name__)

            with app.open_resource('db/Entities.sql') as f:
                cursor.execute(f.read().decode('utf8'))

            with app.open_resource('db/Relationships.sql') as f:
                cursor.execute(f.read().decode('utf8'))

            with app.open_resource('db/SampleData.sql') as f:
                cursor.execute(f.read().decode('utf8'))

    else:
        app = Flask(__name__)
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
