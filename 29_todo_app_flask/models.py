import sqlite3

DB_NAME = 'database.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
                    CREATE TABLE IF NOT EXISTS todos(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     title TEXT NOT NULL,
                     completed INTEGER NOT NULL DEFAULT 0 CHECK (completed IN (0, 1))
                     )
                    ''')

def insert_todo(title):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            '''
            INSERT INTO todos(title)
            VALUES(?)
            ''',
            (title,)
        )
        return cursor.lastrowid

def get_todos():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('SELECT id, title, completed FROM todos')
        return cur.fetchall()