# app.py

import streamlit as st
from neo4j_operations import check_songs_in_neo4j, get_song_from_neo4j
from genius_api import get_full_lyrics
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

# Streamlit UI
st.set_page_config(page_title="🎶 Lyrics Chatbot", page_icon="🎤")

# Title and Info
st.title("🎤 Lyrics Chatbot")
st.info("Ask me about your favorite Bollywood songs! 🎵", icon="ℹ️")

# Add a stylized container
with st.container():
    st.image("https://png.pngtree.com/png-clipart/20230401/original/pngtree-smart-chatbot-cartoon-clipart-png-image_9015126.png", width=100)
    song_title = st.text_input("🎶 Enter Song Title", placeholder="Enter the song name")

    # Add a submit button
    if st.button("🔍 Search"):
        if song_title:
            song_data = get_song_from_neo4j(song_title)
            
            if song_data:
                st.subheader(f"🎶 Song: {song_data['title']}")
                st.write(f"👤 Singer: {song_data['singer']}")
                st.write(f"📅 Year: {song_data['year']}")
                st.write(f"🎵 Genre: {song_data['genre']}")
                st.write(f"✍️ Lyrics: {song_data['lyrics'][:200]}...")  # Display first 200 chars of lyrics
                
                # Get full lyrics from Genius
                lyrics_url = get_full_lyrics(song_data['title'])
                if lyrics_url:
                    st.write(f"[📖 Full Lyrics on Genius]({lyrics_url})")
                else:
                    st.write("⚠️ Full lyrics not found on Genius.")
            else:
                st.write("❌ Song not found in the database.")
        else:
            st.warning("⚠️ Please enter a song title.")

# Test Neo4j connection on startup
try:
    from neo4j_operations import driver
    driver.verify_connectivity()
    print("Successfully connected to Neo4j.")
except Exception as e:
    print(f"Failed to connect to Neo4j: {e}")
