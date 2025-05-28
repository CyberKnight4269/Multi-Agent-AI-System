import sqlite3
from datetime import datetime

class MemoryStore:
    def __init__(self, db_path="memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS logs (
            timestamp TEXT,
            source TEXT,
            format TEXT,
            intent TEXT,
            agent TEXT,
            sender TEXT,
            urgency TEXT
        )''')
        self.conn.commit()

    def log(self, data):
        self.conn.execute('''INSERT INTO logs 
            (timestamp, source, format, intent, agent, sender, urgency) 
            VALUES (?, ?, ?, ?, ?, ?, ?)''', (
                datetime.utcnow().isoformat(),
                data.get("source"),
                data.get("format"),
                data.get("intent"),
                data.get("agent"),
                data.get("sender"),
                data.get("urgency")
            ))
        self.conn.commit()

    def show(self):
        cursor = self.conn.execute("SELECT * FROM logs ORDER BY timestamp DESC")
        for row in cursor.fetchall():
            print(row)

memory_store = MemoryStore()