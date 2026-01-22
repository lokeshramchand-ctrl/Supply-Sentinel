#!/usr/bin/env python3
"""
Seed database with sample supply chain data.
Run: python seed_data.py
"""

import sqlite3
import json
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "storage" / "agent_logs.db"

# Sample seed data
SAMPLE_ORDERS = [
    {
        "order_id": "ORD-2026-001",
        "supplier": "TechSupply Co.",
        "expected_delivery": (datetime.utcnow() + timedelta(days=5)).isoformat(),
        "current_status": "In Transit",
        "thought": "Order from reliable supplier, on schedule",
        "decision": "LOG_ONLY",
        "tools_used": ["supplier_check", "delivery_tracker"]
    },
    {
        "order_id": "ORD-2026-002",
        "supplier": "GlobalParts Inc.",
        "expected_delivery": (datetime.utcnow() - timedelta(days=2)).isoformat(),
        "current_status": "Delayed",
        "thought": "Delivery overdue by 2 days, supplier not responding",
        "decision": "NOTIFY",
        "tools_used": ["delay_detector", "supplier_contact"]
    },
    {
        "order_id": "ORD-2026-003",
        "supplier": "RapidShip Ltd.",
        "expected_delivery": (datetime.utcnow() + timedelta(days=3)).isoformat(),
        "current_status": "Processing",
        "thought": "High-value order, monitoring closely",
        "decision": "LOG_ONLY",
        "tools_used": ["order_validator", "risk_analyzer"]
    },
    {
        "order_id": "ORD-2026-004",
        "supplier": "EmergeSupply LLC",
        "expected_delivery": (datetime.utcnow() - timedelta(days=7)).isoformat(),
        "current_status": "Cancelled",
        "thought": "Order cancelled, supplier breach detected",
        "decision": "ESCALATE",
        "tools_used": ["breach_detector", "escalation_protocol"]
    },
]

def seed_database():
    """Insert sample data into database"""
    DB_PATH.parent.mkdir(exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Ensure table exists
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
    
    # Insert sample data
    for order in SAMPLE_ORDERS:
        c.execute("""
            INSERT INTO agent_logs (timestamp, input, thought, decision, tools_used)
            VALUES (?, ?, ?, ?, ?)
        """, (
            datetime.utcnow().isoformat(),
            json.dumps({
                "order_id": order["order_id"],
                "supplier": order["supplier"],
                "expected_delivery": order["expected_delivery"],
                "current_status": order["current_status"]
            }),
            order["thought"],
            order["decision"],
            json.dumps(order["tools_used"])
        ))
    
    conn.commit()
    conn.close()
    
    print(f"✓ Seeded {len(SAMPLE_ORDERS)} sample orders")

def clear_database():
    """Clear all data from agent_logs table"""
    if not DB_PATH.exists():
        print("Database not found")
        return
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM agent_logs")
    conn.commit()
    
    # Get count
    c.execute("SELECT COUNT(*) FROM agent_logs")
    count = c.fetchone()[0]
    conn.close()
    
    print(f"✓ Database cleared. Rows remaining: {count}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "clear":
        clear_database()
    else:
        seed_database()
