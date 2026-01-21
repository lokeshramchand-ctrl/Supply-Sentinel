import sqlite3
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "storage" / "agent_logs.db"

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS agent_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            input TEXT,
            thought TEXT,
            decision TEXT,
            tools_used TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_agent_run(input_data, thought, decision, tools_used):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO agent_logs (timestamp, input, thought, decision, tools_used)
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.utcnow().isoformat(),
        json.dumps(input_data),
        thought,
        decision,
        json.dumps(tools_used)
    ))
    conn.commit()
    conn.close()
