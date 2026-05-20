import sqlite3
from db_handler import syslog as log

DB_PATH = "nova_pets.db"

def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # zodat je kolommen op naam kunt ophalen
        return conn
    except sqlite3.Error as e:
        print(log.ERROR_CONNECTION_FAILED + f" ({e})")
        return None