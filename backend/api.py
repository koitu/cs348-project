from flask import Flask
from flask_cors import CORS

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


if __name__ == "__main__":
    app.run()