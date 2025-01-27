
# Spotify Playlist Randomizer

This Python script interacts with Spotify's API to queue a set of random tracks from a playlist and optionally add a specific song to the queue.

## Prerequisites

Before using this script, ensure you have the following:

1.  **Spotify Developer Account**: You need to create a Spotify Developer app to obtain the `Client ID` and `Client Secret`.
2.  **Python Installed**: Ensure Python 3.7+ is installed on your system.
3.  **Spotify Premium**: The script requires a Spotify Premium account for queue management.

## Installation

1.  Clone or download this repository to your local machine.
    
2.  Install the required dependencies by running:
``` bash
pip install -r requirements.txt
``` 
3. Update the following variables in the script (`app.py`) with your details:

-   `SPOTIFY_CLIENT_ID`
-   `SPOTIFY_CLIENT_SECRET`
-   `SPOTIFY_REDIRECT_URI`
-   `PLAYLIST_URI`
-   `SPECIFIC_SONG_URI`

## Usage

### Run the Script

To run the script, execute the provided batch file or run the Python script directly:

#### Using Batch File

Double-click the `start.bat` file.

#### Directly via Python

Execute the script from the terminal:
```bash
python app.py
```

Here’s a `README.md` file to explain how to use your Python script:

----------

# Spotify Playlist Randomizer

This Python script interacts with Spotify's API to queue a set of random tracks from a playlist and optionally add a specific song to the queue.

## Prerequisites

Before using this script, ensure you have the following:

1.  **Spotify Developer Account**: You need to create a Spotify Developer app to obtain the `Client ID` and `Client Secret`.
2.  **Python Installed**: Ensure Python 3.7+ is installed on your system.
3.  **Spotify Premium**: The script requires a Spotify Premium account for queue management.

## Installation

1.  Clone or download this repository to your local machine.
    
2.  Install the required dependencies by running:
    
    ```bash
    `pip install -r requirements.txt` 
    ```
3.  Update the following variables in the script (`app.py`) with your details:
    
    -   `SPOTIFY_CLIENT_ID`
    -   `SPOTIFY_CLIENT_SECRET`
    -   `SPOTIFY_REDIRECT_URI`
    -   `PLAYLIST_URI`
    -   `SPECIFIC_SONG_URI`

[How to get the Spotify Client ID & Secret](https://stevesie.com/docs/pages/spotify-client-id-secret-developer-api)

## Usage

### Run the Script

To run the script, execute the provided batch file or run the Python script directly:

#### Using Batch File

Double-click the `start.bat` file.

#### Directly via Python
``` bash
python app.py
``` 

### Behavior

1.  The script fetches tracks from the specified playlist (`PLAYLIST_URI`).
2.  A random selection of tracks (based on `NUMBER_OF_RANDOM_SONGS`) is added to your Spotify queue.
3.  Optionally, a specific track (`SPECIFIC_SONG_URI`) is added to the queue if `NUMBER_OF_RANDOM_SONGS` is set, not null, or empty.
4.  Tracks will appear in your Spotify app's play queue.

## Notes

-   Ensure the `SPOTIFY_REDIRECT_URI` matches the one configured in your Spotify Developer Dashboard.
-   If any issues occur with queuing tracks, the script will print an error message.

### Disclaimer:
This software is provided "as is", without any warranties or guarantees of any kind. Use it at your own risk.
For the full terms of the AGPLv3 license, refer to the  [official license text](https://www.gnu.org/licenses/agpl-3.0.html).