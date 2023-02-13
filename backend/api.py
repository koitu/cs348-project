from flask import Flask
from flask_cors import CORS
from dataModel import dataModel
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return """

            <form action="/members">
                <input type="submit" value="Go to new path">
            </form>

            """

@app.route("/members")
def members():
    return {"players" : ["Ali", "Shayan", "Arvin", "Kiarash"]}

@app.route("/keyword/<given>")
def keyword(given):
    return dataModel().getWithKeywords(given)

@app.route("/getUser/<id>/<pass>")
def getUser(id: str, passw: str):
    return dataModel.getUserData(id)

if __name__ == "__main__":
    app.run()