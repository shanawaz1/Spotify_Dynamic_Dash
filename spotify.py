import os
import tempfile
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set environment variables
os.environ['SPOTIPY_CLIENT_ID'] = '2c196661567b425c9a210f7d8d1a2c7b'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'fafd037013a24d4a8692452e4651449f'

# Use a temp directory to avoid .cache warnings
os.environ['SPOTIPY_CLIENT_CREDENTIALS_CACHE'] = os.path.join(tempfile.gettempdir(), ".spotipy_cache")

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# Load the CSV file
df = pd.read_csv("C:/Users/shana/RecordsFiltered_TrustRegion/spotify-2023.csv", encoding='latin1')

# Function to fetch album cover URL
def get_cover_url(track, artist):
    try:
        results = sp.search(q=f'track:{track} artist:{artist}', type='track', limit=1)
        return results['tracks']['items'][0]['album']['images'][0]['url']
    except Exception as e:
        return None

# Apply the function to each row
df['album_cover_url'] = df.apply(lambda row: get_cover_url(row['track_name'], row['artist(s)_name']), axis=1)

# Optional: Save to a new CSV file
df.to_csv("C:/Users/shana/RecordsFiltered_TrustRegion/spotify-2023-with-covers.csv", index=False)

# Preview
print(df[['track_name', 'artist(s)_name', 'album_cover_url']].head())
