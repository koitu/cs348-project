from flask import Flask
from flask_cors import CORS
from dataModel import dataModel

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return dataModel.metaData()


@app.route("/keyword/<given>")
def keyword(given):
    return dataModel().getWithKeywords(given)


@app.route("/getUser/<id>")
def getUser(id: str):
    return dataModel.getUserData(id)


@app.route("/getPlayer/<id>")
def getPlayer(id: str):
    return dataModel().getPlayerData(id)


@app.route("/getTeam/<id>")
def getTeam(id: str):
    return dataModel.getPlayerData(id)


if __name__ == "__main__":
    from api import match, player, team, user

    app.register_blueprint(match.bp, url_prefix='/api/matches')
    app.register_blueprint(player.bp, url_prefix='/api/players')
    app.register_blueprint(team.bp, url_prefix='/api/teams')
    app.register_blueprint(user.bp, url_prefix='/api/users')

    app.run()
