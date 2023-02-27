from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


if __name__ == "__main__":
    from api import match, player, team, user

    app.register_blueprint(match.bp, url_prefix='/api/matches')
    app.register_blueprint(player.bp, url_prefix='/api/players')
    app.register_blueprint(team.bp, url_prefix='/api/teams')
    app.register_blueprint(user.bp, url_prefix='/api/users')

    app.run()
