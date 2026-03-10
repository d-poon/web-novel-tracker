import sqlite3
from pathlib import Path

DB_NAME = Path("runtime/data")
DB_NAME.mkdir(exist_ok=True)

DB_NAME = DB_NAME / "novels.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
