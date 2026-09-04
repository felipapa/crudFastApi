import sqlite3


def get_connection():
    conn = sqlite3.connect("x.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()


def initDb():
    conn = sqlite3.connect("x.db")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, stock INTEGER, precio REAL)"
    )
    conn.commit()
    conn.close()

