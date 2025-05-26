import sqlite3

CONN = sqlite3.connect('db/articles.db')
CURSOR = CONN.cursor()

def get_connection():
    return CONN, CURSOR
