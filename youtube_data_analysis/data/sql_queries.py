# data/sql_queries.py

# Query to create table for storing YouTube data
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS youtube_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    channel_name VARCHAR(255),
    channel_id VARCHAR(255),
    subscribers INT,
    total_videos INT,
    playlist_id VARCHAR(255),
    video_id VARCHAR(255),
    video_name VARCHAR(255),
    likes INT,
    dislikes INT,
    comments INT,
)
"""

# Query to insert data into YouTube data table
INSERT_QUERY = """
    INSERT INTO youtube_data 
    (channel_name, channel_id, subscribers, total_videos, playlist_id, video_id, video_name, likes, dislikes, comments) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
SELECT_ALL_QUERY = """
    SELECT * FROM youtube_data
"""


# Example select query; replace with actual queries as per your needs
SELECT_ALL_QUERY = """
SELECT * FROM youtube_data
"""
