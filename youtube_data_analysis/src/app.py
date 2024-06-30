import sys
import streamlit as st
import pandas as pd

# Add your project root directory to the Python path
sys.path.insert(0, 'C:\\Users\\Lenovo\\Desktop\\youtube_data_analysis')

# Import necessary functions and constants
from data.db_utils import create_connection, execute_query, fetch_data
from data.sql_queries import INSERT_QUERY, SELECT_ALL_QUERY
from src.youtube_api import API_KEY, CHANNEL_ID, fetch_channel_data

# Constants for MySQL connection (replace with your actual MySQL credentials)
HOST = 'DESKTOP-B2E6EGI'
USER = 'root'
PASSWORD = '1234'
DATABASE = 'youtube_data_db'

# Function to initialize database connection
def init_db():
    return create_connection(HOST, USER, PASSWORD, DATABASE)

# Streamlit UI
def main():
    st.title('YouTube Data Analysis App')

    # Inside the button click handler for 'Fetch and Store Data'
if st.button('Fetch and Store Data'):
    # Fetch channel data from YouTube API
    channel_data = fetch_channel_data(API_KEY, CHANNEL_ID)
    
    # Extract relevant data from API response
    channel_name = channel_data['items'][0]['snippet']['title']
    channel_id = CHANNEL_ID
    subscribers = int(channel_data['items'][0]['statistics']['subscriberCount'])
    total_videos = int(channel_data['items'][0]['statistics']['videoCount'])
    playlist_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Simulated video data (replace with actual video data retrieval)
    videos = [
        {
            'video_id': 'V1234567890',
            'video_name': 'Video 1',
            'likes': 100,
            'dislikes': 10,
            'comments': 20
        },
        {
            'video_id': 'V2345678901',
            'video_name': 'Video 2',
            'likes': 200,
            'dislikes': 20,
            'comments': 30
        }
    ]

    # Connect to database
    connection = init_db()
    if connection:
        # Insert channel data into MySQL
        channel_insert_data = (channel_name, channel_id, subscribers, total_videos, playlist_id, '', '', 0, 0, 0)
        execute_query(connection, INSERT_QUERY, channel_insert_data)
        
        # Insert video data into MySQL
        for video in videos:
            video_insert_data = (channel_name, channel_id, subscribers, total_videos, playlist_id,
                                 video['video_id'], video['video_name'], video['likes'], video['dislikes'], video['comments'])
            execute_query(connection, INSERT_QUERY, video_insert_data)

        st.success('Data fetched and stored successfully.')

