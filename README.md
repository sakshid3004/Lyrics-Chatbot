# 🎵 Lyrics Chatbot (Neo4j + Python)

A smart Lyrics Chatbot that allows users to search and interact with Bollywood song lyrics using a Neo4j Knowledge Graph and Python.

---

## 🚀 Features
- Search lyrics by song name
- Fetch song details (title, singer, movie, year)
- Graph-based data storage using Neo4j
- API integration using Genius API
- CSV-based song dataset

---

## 🛠️ Tech Stack
- Python
- Neo4j (Graph Database)
- Genius API
- Git & GitHub

---

## 📁 Project Structure
Lyrics-Chatbot/
│
├── app.py
├── config.py
├── genius_api.py
├── neo4j_operations.py
├── songs.csv
├── README.md

---

## ⚙️ Setup Instructions (Windows)

### 1️⃣ Clone Repository
```bash
git clone https://github.com/sakshi3004/Lyrics-Chatbot.git
cd Lyrics-Chatbot

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

***###3️⃣ Install Dependencies***
pip install -r requirements.txt

***###4️⃣ Configure Neo4j***

Install Neo4j Desktop

Create a database

Update credentials in config.py

NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

***###5️⃣ Genius API Setup***

Create Genius API token

Add it in config.py

GENIUS_API_KEY=your_genius_api_key

***###6️⃣ Run the Application***
python app.py

📌 Future Enhancements

Streamlit Web UI

Mood-based recommendations

LLM integration

User authentication

***👩‍💻 Author***

Sakshi Darekar
MSc Computer Science
