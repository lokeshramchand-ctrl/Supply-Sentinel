import sqlite3
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "storage" / "agent_logs.db"

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
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
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
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

    
def fetch_agent_history(limit: int = 50):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()

    c.execute("""
        SELECT timestamp, input, thought, decision, tools_used
        FROM agent_logs
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = c.fetchall()
    conn.close()

    history = []
    for row in rows:
        history.append({
            "timestamp": row[0],
            "input": json.loads(row[1]),
            "thought": row[2],
            "decision": row[3],
            "tools_used": json.loads(row[4]),
        })

    return history
