## ⚠️ Project in Progress
After lots of troubleshotting and continuously receiving a 403 error when trying to fetch audio features from Spotify’s API, I realised that the _get audio features method_ is being deprecated and I am not able to bypass the issues as they are on the libraries side. Keeping this repository for learning sake. ~~Playlist data loads correctly, but some endpoints are restricted — likely due to token or account permission. issues.~~

# 🎧 Spotify Playlist Data Enrichment with Audio Features

I pulled playlists four  from the Spotify API curated by music labels and enriched them with additional audio features.

## 📌 Project Summary
- ✅ Loaded data from 4 Spotify playlists containing tracks with:
  - track_name
  - artist_name
  - playlist_name
- ✅ Added track metadata:
  - track_id
  - explicit flag
  - duration_ms
- ✅ Retrieved audio features for each track:
  - music key
  - mode (major/ minor)
  - tempo (BPM)
  - speechiness (measure of spoken words)
  - instrumentalness (measure of how instrumental the track is)
- ✅ ~~Generated an enriched CSV output file containing:~~
  - ~~Original track details (name, artist, playlist)~~
  - ~~Additional metadata (track ID, explicit flag, duration)~~
  - ~~Audio features (key, mode, tempo, speechiness, instrumentalness)~~
