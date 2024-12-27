import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector

# Step 1: Set up Spotify API credentials
# Replace the placeholders with your Spotify API client credentials.
# These are required to authenticate with the Spotify API.
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='your_client_id',  # Your Spotify Client ID
    client_secret='your_secret_key'  # Your Spotify Client Secret
))

# Step 2: Configure MySQL database connection
# Update these details to match your MySQL server credentials and database name.
db_config = {
    'host': 'localhost',           # Hostname or IP address of your MySQL server
    'user': 'your_user_name',                # MySQL username
    'password': 'your_password',            # MySQL password
    'database': 'spotify_db'       # Database name where the tracks will be stored
}

# Step 3: Establish a connection to the MySQL database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Step 4: Read track URLs from a file
# This file contains one Spotify track URL per line.
file_path = "track_urls.txt"  # Path to the file containing track URLs
with open(file_path, 'r') as file:
    track_urls = file.readlines()  # Read all lines from the file

# Step 5: Process each track URL
for track_url in track_urls:
    # Remove any leading or trailing whitespace from the URL
    track_url = track_url.strip()
    try:
        # Extract the track ID from the Spotify URL using regex
        track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

        # Fetch track details from the Spotify API using the track ID
        track = sp.track(track_id)

        # Extract key metadata from the track
        track_data = {
            'Track Name': track['name'],  # Name of the track
            'Artist': track['artists'][0]['name'],  # Name of the primary artist
            'Album': track['album']['name'],  # Album name
            'Popularity': track['popularity'],  # Popularity score (0-100)
            'Duration (minutes)': track['duration_ms'] / 60000  # Convert duration from milliseconds to minutes
        }

        # Define an SQL query to insert the track data into the database
        insert_query = """
        INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Execute the query and pass the track data as parameters
        cursor.execute(insert_query, (
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (minutes)']
        ))

        # Commit the transaction to save the changes to the database
        connection.commit()

        # Notify the user about the successful insertion
        print(f"Inserted: {track_data['Track Name']} by {track_data['Artist']}")

    except Exception as e:
        # Handle errors, such as invalid URLs or API issues, and notify the user
        print(f"Error processing URL: {track_url}, Error: {e}")

# Step 6: Close the database connection
# Always close the cursor and connection to free up resources.
cursor.close()
connection.close()

# Final message indicating all tracks have been processed
print("All tracks have been processed and inserted into the database.")