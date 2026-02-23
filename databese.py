import sqlite3

conn = sqlite3.connect("game.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS game_state (
    guild_id INTEGER PRIMARY KEY,
    data TEXT
)
""")

conn.commit()
