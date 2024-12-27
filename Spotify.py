# Import necessary libraries
from spotipy.oauth2 import SpotifyClientCredentials  # To authenticate and fetch data from Spotify
import spotipy  # Main Spotify Web API library
import pandas as pd  # For handling data in a tabular format
import matplotlib.pyplot as plt  # For visualizing data
import re  # For extracting the track ID from the URL

# Set up Spotify Client Credentials
# Replace with your actual Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='your_client_id',  # Replace with your Client ID
    client_secret='your_client_secret_key'  # Replace with your Client Secret
))

# URL of the Spotify track (replace with the desired track URL)
track_url = "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp"

# Extract the track ID from the URL using regex
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Fetch track details using Spotify Web API
track = sp.track(track_id)

# Extract and organize relevant metadata
track_data = {
    'Track Name': track['name'],  # Name of the track
    'Artist': track['artists'][0]['name'],  # Name of the primary artist
    'Album': track['album']['name'],  # Album name
    'Popularity': track['popularity'],  # Popularity score (0-100)
    'Duration (minutes)': track['duration_ms'] / 60000  # Convert duration from milliseconds to minutes
}

# Display metadata in the console
print("\nExtracted Track Metadata:")
print(f"Track Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (minutes)']:.2f} minutes")

# Convert metadata to a pandas DataFrame for easier manipulation
df = pd.DataFrame([track_data])

# Print the DataFrame
print("\nTrack Data as DataFrame:")
print(df)

# Save metadata to a CSV file
df.to_csv('spotify_track_data.csv', index=False)
print("\nTrack metadata saved to 'spotify_track_data.csv'")

# Visualize track metadata using a bar chart
# Features to visualize
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

# Plot the bar chart
plt.figure(figsize=(8, 5))  # Set the size of the figure
plt.bar(features, values, color='skyblue', edgecolor='black')  # Create a bar chart
plt.title(f"Track Metadata for '{track_data['Track Name']}'")  # Set the title
plt.ylabel('Value')  # Label for the Y-axis
plt.show()  # Display the plot