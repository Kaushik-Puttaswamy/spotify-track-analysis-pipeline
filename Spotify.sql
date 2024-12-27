-- Step 1: Create the database
-- This command creates a database named "spotify_db".
CREATE DATABASE spotify_db;

-- Step 2: Select the database to use
-- This command sets "spotify_db" as the active database for the subsequent operations.
USE spotify_db;

-- Step 3: Create the "spotify_tracks" table
-- This command creates a table named "spotify_tracks" with columns for:
-- 1. `id` - A unique identifier for each track (Primary Key, auto-incremented).
-- 2. `track_name` - The name of the track (VARCHAR type, max 255 characters).
-- 3. `artist` - The name of the artist (VARCHAR type, max 255 characters).
-- 4. `album` - The name of the album (VARCHAR type, max 255 characters).
-- 5. `popularity` - The track's popularity (integer value).
-- 6. `duration_minutes` - The track's duration in minutes (float value).
CREATE TABLE IF NOT EXISTS spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
);

-- Step 4: Retrieve all records from the "spotify_tracks" table
-- This query selects all columns and rows from the "spotify_tracks" table for inspection.
SELECT * FROM spotify_tracks;

-- Step 5: Retrieve the most popular track
-- This query selects the name, artist, album, and popularity of the most popular track.
-- It orders the tracks by popularity in descending order and limits the result to one row.
SELECT track_name, artist, album, popularity
FROM spotify_tracks
ORDER BY popularity DESC
LIMIT 1;

-- Step 6: Calculate the average popularity of tracks
-- This query calculates the average popularity of all tracks in the "spotify_tracks" table.
SELECT AVG(popularity) AS average_popularity
FROM spotify_tracks;

-- Step 7: Retrieve tracks longer than 4 minutes
-- This query selects the name, artist, and duration (in minutes) of tracks whose duration exceeds 4 minutes.
SELECT track_name, artist, duration_minutes
FROM spotify_tracks
WHERE duration_minutes > 4.0;

-- Step 8: Categorize tracks by popularity range
-- This query categorizes tracks into three groups based on their popularity:
-- 1. 'Very Popular' for tracks with popularity >= 80.
-- 2. 'Popular' for tracks with popularity between 50 and 79.
-- 3. 'Less Popular' for tracks with popularity below 50.
-- It also counts the number of tracks in each category.
SELECT 
    CASE 
        WHEN popularity >= 80 THEN 'Very Popular'
        WHEN popularity >= 50 THEN 'Popular'
        ELSE 'Less Popular'
    END AS popularity_range,
    COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY popularity_range;