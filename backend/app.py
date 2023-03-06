from flask import Flask
from flask_cors import CORS
# from flaskext.mysql import MySQL
# from flask_mysqldb import MySQL

import click


app = Flask(__name__)
CORS(app)

# app.config['MYSQL_DATABASE_HOST'] = "127.0.0.1"
# app.config['MYSQL_DATABASE_USER'] = "root"
# app.config['MYSQL_DATABASE_PORT'] = "5555"
# app.config['MYSQL_DATABASE_PASSWORD'] = "password"
# app.config['MYSQL_DATABASE_DB'] = 'cs348'
# mysql = MySQL()

# mysql = MySQL(app,
#               prefix="database",
#               host="localhost:5555",
#               user="root",
#               password="password",
#               autocommit=True
# )

# mysql.init_app(app)

# @click.command('init-db')
# def init_db():
#     conn = mysql.connect()
#     cursor = conn.cursor()


if __name__ == "__main__":
    from api import match, player, team, user

    app.register_blueprint(match.bp, url_prefix='/api/matches')
    app.register_blueprint(player.bp, url_prefix='/api/players')
    app.register_blueprint(team.bp, url_prefix='/api/teams')
    app.register_blueprint(user.bp, url_prefix='/api/users')

    app.run()
