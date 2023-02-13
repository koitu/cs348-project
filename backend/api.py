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
    app.run()