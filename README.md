# spotify-track-analysis-pipeline

# Spotify Track Analysis Pipeline

This repository contains a pipeline for analyzing Spotify track data using the Spotify Web API. The project collects track metadata, stores it in a MySQL database, and provides insights via visualizations and SQL queries. The pipeline consists of several components, including Python scripts and MySQL queries for database management.

## Project Files Overview

### 1. **`Spotify.py`**
   - A Python script that connects to the Spotify Web API, extracts track data (e.g., track name, artist, album, popularity, and duration), and displays it. The data is also saved to a CSV file and visualized as a bar chart.

### 2. **`Spotify_mysql.py`**
   - This Python script connects to a MySQL database and inserts the extracted track metadata into a `spotify_tracks` table. It retrieves track data from the Spotify API and stores it for future querying.

### 3. **`Spotify_mysql_urls.py`**
   - A Python script that processes a list of Spotify track URLs stored in a file (`track_urls.txt`). It extracts metadata for each track and inserts the data into the MySQL database.

### 4. **`Spotify.sql`**
   - Contains SQL commands for creating the `spotify_db` database, creating the `spotify_tracks` table, and several queries for analyzing the track data in the database. These queries include fetching the most popular tracks, calculating average popularity, and categorizing tracks by popularity range.

### 5. **`track_urls.txt`**
   - A text file containing a list of Spotify track URLs. Each URL represents a track whose metadata will be extracted and stored in the database.

### 6. **`spotify_track_data.csv`**
   - A CSV file that stores the metadata of a Spotify track (such as track name, artist, album, popularity, and duration in minutes).

### 7. **Figures**
   - **`Spotify_Data_Pipeline_Architecture.png`**: An architecture diagram illustrating the flow of data in the Spotify track analysis pipeline.
   - **`Figure_1.png`**: A diagram showcasing the structure of the track analysis pipeline.
   - **`Spotify for developers Web API UI.png`**: A screenshot of the Spotify Developer Dashboard UI, where you can manage your Spotify API credentials.

---

## How to Set Up and Use the Project

### Prerequisites
- Python 3.x
- MySQL Database
- Spotify Developer Account (to generate API credentials)

### 1. **Install Dependencies**

Use the `requirements.txt` file to install all necessary libraries for the project:

```bash
pip install -r requirements.txt

