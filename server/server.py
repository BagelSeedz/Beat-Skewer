from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api import Spotify, Features


app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Spotify, "/spotify-token")
api.add_resource(Features, "/audio-features")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()