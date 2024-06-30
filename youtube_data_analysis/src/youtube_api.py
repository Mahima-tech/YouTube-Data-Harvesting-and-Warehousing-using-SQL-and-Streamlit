# src/youtube_api.py

from googleapiclient.discovery import build
import json

# Replace with your actual API key
API_KEY = 'AIzaSyC5Bstaaheb7BQkOfcBWme5ejNuz81ot6M'

# Replace with your actual Channel ID
CHANNEL_ID = 'UCaqDu9xbvQv8JGTcnzlsc1Q'

# Function to fetch channel data from YouTube API
def fetch_channel_data(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    response = request.execute()
    return response

# Example usage
if __name__ == '__main__':
    channel_data = fetch_channel_data(API_KEY, CHANNEL_ID)
    print(json.dumps(channel_data, indent=2))
