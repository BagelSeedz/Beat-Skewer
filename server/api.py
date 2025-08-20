from flask_restful import Resource, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class Spotify(Resource):
    def get(self):
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

        res = requests.post(
            url="https://accounts.spotify.com/api/token",
            headers = {"Content-Type": "application/x-www-form-urlencoded"},
            data=f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
        )

        return res.json()

class Features(Resource):
    def get(self):
        track_id = request.args.get("track_id")
        if not track_id:
            return {"message": "Missing track ID"}, 404
        
        res = requests.get(
            url=f"https://track-analysis.p.rapidapi.com/pktx/spotify/{track_id}",
            headers={
                "x-rapidapi-key": os.getenv("X_RAPID_API_KEY"),
                "x-rapidapi-host": 'track-analysis.p.rapidapi.com'
            }
        )
        
        return res.json()