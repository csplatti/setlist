import requests
from dotenv import dotenv_values
import spotipy
from spotipy.oauth2 import SpotifyOAuth

config = dotenv_values(".env")

# OAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=config["SPOTIFY_CLIENT_ID"],
    client_secret=config["SPOTIFY_CLIENT_SECRET"],
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-library-read playlist-read-private"
))

# now just use it
tracks = sp.current_user_saved_tracks()

print(tracks.keys())
print(tracks["items"][0]["track"]["name"])
for track in tracks["items"]:
    print(track["track"]["name"])


all_tracks = []
results = sp.current_user_saved_tracks(limit=50)
all_tracks.extend(results['items'])

while results['next']:
    results = sp.next(results)
    all_tracks.extend(results['items'])

print(f"Got {len(all_tracks)} tracks")

for track in all_tracks:
    print(track["track"]["name"])


# # Request Playlist Information
# response = requests.get("https://api.spotify.com/v1/playlists/4adxOYH8155FNqKGWyuVwO?si=d822c6443b9a4283/items", 
#                        headers={"Authorization": f"Bearer {config["SPOTIFY_ACCESS_TOKEN"]}"})

# data = response.text

# with open("response.json", "a") as f:
#   f.write(data)