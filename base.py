import sqlite3


def get_connection():
    conn = sqlite3.connect("x.db")
    conn.row_factory = sqlite3.Row
    return conn


def initDb():
    conexion = get_connection()
    conexion.execute(
        "CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, stock INTEGER, precio REAL)"
    )
    conexion.commit()  
    conexion.close()

