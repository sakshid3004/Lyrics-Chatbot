# genius_api.py

import requests
from config import GENIUS_API_KEY

def get_full_lyrics(song_title):
    base_url = f"https://api.genius.com/search?q={song_title}"
    headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
    response = requests.get(base_url, headers=headers)
    data = response.json()
    
    if data["response"]["hits"]:
        song_url = data["response"]["hits"][0]["result"]["url"]
        return song_url
    return None
