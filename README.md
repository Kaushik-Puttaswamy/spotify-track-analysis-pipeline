# spotify-track-analysis-pipeline

# Spotify Track Analysis Pipeline

This repository contains a pipeline for analyzing Spotify track data using the Spotify Web API. The project collects track metadata, stores it in a MySQL database, and provides insights via visualizations and SQL queries. The pipeline consists of several components, including Python scripts and MySQL queries for database management.

## 1. Project Files Overview

### 1.1 **`Spotify.py`**
   - A Python script that connects to the Spotify Web API, extracts track data (e.g., track name, artist, album, popularity, and duration), and displays it. The data is also saved to a CSV file and visualized as a bar chart.

### 1.2 **`Spotify_mysql.py`**
   - This Python script connects to a MySQL database and inserts the extracted track metadata into a `spotify_tracks` table. It retrieves track data from the Spotify API and stores it for future querying.

### 1.3 **`Spotify_mysql_urls.py`**
   - A Python script that processes a list of Spotify track URLs stored in a file (`track_urls.txt`). It extracts metadata for each track and inserts the data into the MySQL database.

### 1.4 **`Spotify.sql`**
   - Contains SQL commands for creating the `spotify_db` database, creating the `spotify_tracks` table, and several queries for analyzing the track data in the database. These queries include fetching the most popular tracks, calculating average popularity, and categorizing tracks by popularity range.

### 1.5 **`track_urls.txt`**
   - A text file containing a list of Spotify track URLs. Each URL represents a track whose metadata will be extracted and stored in the database.

### 1.6 **`spotify_track_data.csv`**
   - A CSV file that stores the metadata of a Spotify track (such as track name, artist, album, popularity, and duration in minutes).

### 1.7 **Figures**
   - **`Spotify_Data_Pipeline_Architecture.png`**: An architecture diagram illustrating the flow of data in the Spotify track analysis pipeline.
   - **`Figure_1.png`**: A diagram showcasing the structure of the track analysis pipeline.
   - **`Spotify for developers Web API UI.png`**: A screenshot of the Spotify Developer Dashboard UI, where you can manage your Spotify API credentials.

---

## 2. How to Set Up and Use the Project

### 2.1 Prerequisites
- Python 3.x
- MySQL Database
- Spotify Developer Account (to generate API credentials)

### 2.2 **Install Dependencies** 
Use the `requirements.txt` file to install all necessary libraries for the project:  

```bash

 pip install -r requirements.txt

```

## 3. Configure Your Spotify API Credentials

In the Python scripts (Spotify.py, Spotify_mysql.py, Spotify_mysql_urls.py), replace the following placeholders with your actual Spotify API credentials:

```
client_id='your_client_id'
client_secret='your_client_secret_key'

```

## 4. Set Up MySQL Database

### 4.1 Create a MySQL database by running the SQL commands from Spotify.sql.
### 4.2 Configure your MySQL connection settings in the Python scripts:
```
db_config = {
    'host': 'localhost',  
    'user': 'your_user_name',  
    'password': 'your_password',  
    'database': 'spotify_db'
}

```

## 5. Check the MySQL Database
After running the Python scripts, you can query the spotify_tracks table in MySQL to analyze and retrieve track data.
```
-- Example query to get the most popular track
SELECT track_name, artist, album, popularity
FROM spotify_tracks
ORDER BY popularity DESC
LIMIT 1;
```

## 6. Visualizations and Figures
Below are the architecture and UI figures used in the project:

### 6.1 Spotify Data Pipeline Architecture
![Spotify Data Pipeline Architecture](https://github.com/Kaushik-Puttaswamy/spotify-track-analysis-pipeline/blob/dev/Spotify_Data_Pipeline_Architecture.png)

### 6.2 Spotify for Developers Web API UI
![Spotify for Developers Web API UI](https://github.com/Kaushik-Puttaswamy/spotify-track-analysis-pipeline/blob/dev/Spotify%20for%20developers%20Web%20API%20UI.png)

### 6.3 Figure 1: Track Analysis Pipeline
![Track Analysis Pipeline](https://github.com/Kaushik-Puttaswamy/spotify-track-analysis-pipeline/blob/main/Figure_1.png)

## 7. Conclusion
This pipeline helps you extract, analyze, and store Spotify track data efficiently. You can visualize the data using bar charts, query it using SQL, and store large datasets in MySQL for more advanced analysis.






