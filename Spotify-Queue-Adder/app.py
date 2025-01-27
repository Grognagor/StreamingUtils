import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
SPOTIFY_CLIENT_ID = "7a9f80272cb64de2b279e6276d24fc92"
SPOTIFY_CLIENT_SECRET = "510e384899df41b98048fc1d8c29b192"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

# Playlist and specific song URIs
PLAYLIST_URI = "7qlDUKxZ3SK4kairaAsBN0"  # Playlist URI from the link
SPECIFIC_SONG_URI = "spotify:track:4y8jTrIvvKKkL0vbn1jo6g"  # Specific song URI from the link
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
