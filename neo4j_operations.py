# neo4j_operations.py

from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

# Connect to Neo4j
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def check_songs_in_neo4j():
    with driver.session() as session:
        result = session.run("MATCH (s:Song) RETURN s.title AS title, s.singer AS singer LIMIT 10")
        songs = result.data()
        return songs

def get_song_from_neo4j(song_title):
    with driver.session() as session:
        result = session.run("""
        MATCH (s:Song)
        WHERE toLower(trim(s.title)) = toLower(trim($title))
        RETURN s.title AS title, s.singer AS singer, s.lyrics AS lyrics, s.link AS link, s.year AS year, s.genre AS genre
        """, title=song_title)
        song = result.single()
        return song
