import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import time

load_dotenv()

client_id=os.getenv('CLIENT_ID'),
client_secret=os.getenv('CLIENT_SECRET'),
redirect_uri=os.getenv('REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    redirect_uri=os.getenv('REDIRECT_URI'),
    scope="playlist-read-private user-library-read"
))

playlist_ids = [
    "2gHETELzVrcADMAD9XOZxH",
    "69lp1rXCWajW2P5rdsLmA2",
    "5TW0jYtGOBfyfIA9p3Huer",
    "3kIY4ckCas4kgUBfyli1SI"
]

all_tracks = []

def fetch_playlist_details(pid):
    try:
        return sp.playlist(pid)['name']
    except Exception as e:
        print(f"Error fetching playlist details for {pid}: {e}")
        return None

for pid in playlist_ids:
    playlist_name = fetch_playlist_details(pid)
    if not playlist_name:
        continue
    try:
        results = sp.playlist_tracks(pid)
        tracks = results['items']

        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        for track in tracks:
            track_name = track['track']['name']
            artist_name = track['track']['artists'][0]['name']
            playlist = sp.playlist(pid)['name']
            track_id = track['track']['id']
            explicit = track['track']['explicit']
            duration = track['track']['duration_ms']

            all_tracks.append({
                'Track Name': track_name,
                'Artist Name': artist_name,
                'Playlist':playlist,
                'Track ID': track_id,
                'Explicit': explicit,
                'Duration (ms)': duration
            })

    except Exception as e:
        print(f"Error fetching tracks for playlist {pid}: {e}")

df_tracks = pd.DataFrame(all_tracks)
track_ids = df_tracks['Track ID'].tolist()

def fetch_audio_features(batch):
    try:
        return sp.audio_features(batch)
    except Exception as e:
        print(f"Error fetching audio features: {e}")
        time.sleep(5)
        return fetch_audio_features(batch)

audio_features = []
for i in range(0, len(track_ids), 50):
    batch = track_ids[i:i+50]
    features = fetch_audio_features(batch)

    features = [feature for feature in features if feature is not None]
    audio_features.extend(features)

df_audio = pd.DataFrame(audio_features)[[
    'id', 'key', 'mode', 'tempo', 'speechiness', 'instrumentalness'
]]
df_audio.rename(columns={'id': 'Track ID'}, inplace=True)

df_final = pd.merge(df_tracks, df_audio, on='Track ID', how='left')

print(df_final.head())

df_final.to_csv("labels_enrichment.csv", index=False)
