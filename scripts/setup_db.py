from lib.db.connection import CONN, CURSOR

def create_tables():
    with open("lib/db/schema.sql") as f:
        CURSOR.executescript(f.read())
    CONN.commit()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
