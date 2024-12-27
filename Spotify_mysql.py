import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Step 1: Set up Spotify API credentials
# Replace the placeholders with your Spotify API credentials.
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='......................',  # Your Spotify Client ID
    client_secret='...........................'  # Your Spotify Client Secret
))

# Step 2: Configure MySQL database connection
# Update these details with your MySQL server credentials and database name.
db_config = {
    'host': 'localhost',           # MySQL host (e.g., localhost)
    'user': 'your_user_name',                # MySQL username
    'password': 'your_password',            # MySQL password
    'database': 'spotify_db'       # MySQL database name
}

# Step 3: Establish a connection to the MySQL database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Step 4: Define the Spotify track URL
# Example URL pointing to a track on Spotify. This will be used to extract track details.
track_url = "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp"

# Step 5: Extract the track ID from the URL
# The track ID is a unique identifier within Spotify URLs, extracted using regex.
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Step 6: Fetch track details from Spotify API
# The `sp.track()` function retrieves detailed information about the track using its ID.
track = sp.track(track_id)

# Step 7: Extract metadata from the track details
# Key attributes like track name, artist, album, popularity, and duration (converted to minutes) are extracted.
track_data = {
    'Track Name': track['name'],  # Name of the track
    'Artist': track['artists'][0]['name'],  # Name of the primary artist
    'Album': track['album']['name'],  # Album name
    'Popularity': track['popularity'],  # Popularity score (0-100)
    'Duration (minutes)': track['duration_ms'] / 60000  # Duration in minutes
}

# Step 8: Insert the track data into the MySQL database
# Define an SQL query to insert the track data into the "spotify_tracks" table.
insert_query = """
INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
VALUES (%s, %s, %s, %s, %s)
"""

# Execute the query using the track data
cursor.execute(insert_query, (
    track_data['Track Name'],       # Track name
    track_data['Artist'],           # Artist name
    track_data['Album'],            # Album name
    track_data['Popularity'],       # Popularity score
    track_data['Duration (minutes)']  # Duration in minutes
))

# Commit the transaction to save the changes
connection.commit()

# Notify the user about the successful insertion of data
print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} inserted into the database.")

# Step 9: Close the database connection
# Always close the cursor and the database connection to free up resources.
cursor.close()
connection.close()