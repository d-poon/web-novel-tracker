import sqlite3
from datetime import date, datetime
from pathlib import Path

DB_NAME = Path("runtime/data")
DB_NAME.mkdir(exist_ok=True)

DB_NAME = DB_NAME / "novels.db"

# Register adapters and converters for date handling
sqlite3.register_adapter(date, lambda d: d.isoformat())
sqlite3.register_converter("DATE", lambda s: date.fromisoformat(s.decode("utf-8")))

sqlite3.register_adapter(datetime, lambda dt: dt.isoformat())
sqlite3.register_converter(
    "TIMESTAMP", lambda s: datetime.fromisoformat(s.decode("utf-8"))
)


def get_connection():
    # Enable detect_types to allow for automatic conversion of DATE and TIMESTAMP fields
    conn = sqlite3.connect(DB_NAME, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn
