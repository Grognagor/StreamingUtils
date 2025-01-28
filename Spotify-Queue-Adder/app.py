import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
SPOTIFY_CLIENT_ID = "ABC123" # Change this to your secret
SPOTIFY_CLIENT_SECRET = "ABC123" # Change this to your secret
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

# Playlist and specific song URIs
PLAYLIST_URI = "ABC123"  # Playlist URI from the link
SPECIFIC_SONG_URI = ""  # Specific song URI from the link
NUMBER_OF_RANDOM_SONGS = 3

scope = "user-read-playback-state user-modify-playback-state playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope=scope))


playlist_tracks = sp.playlist_tracks(PLAYLIST_URI)
track_uris = [track['track']['uri'] for track in playlist_tracks['items']]

random_tracks = random.sample(track_uris, NUMBER_OF_RANDOM_SONGS)

for track in random_tracks:
    sp.add_to_queue(track)


if 'NUMBER_OF_RANDOM_SONGS' in globals() and NUMBER_OF_RANDOM_SONGS:
    try:
        sp.add_to_queue(SPECIFIC_SONG_URI)
        print("Specific song added to the queue successfully.")
    except spotipy.SpotifyException as e:
        print(f"Failed to add the specific song to the queue: {e}")

print("Tracks enqueued successfully!")
