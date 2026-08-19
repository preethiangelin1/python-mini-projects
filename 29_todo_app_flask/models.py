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
    
def get_todos_by_status(completed):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute(
            """
            SELECT id, title, completed
            FROM todos
            WHERE completed = ?
            """,
            (1 if completed else 0,)
        )

        return cur.fetchall()

def get_todo(id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute('SELECT id, title, completed FROM todos  WHERE id = ?', (id,))
        return cursor.fetchone()

def delete_todo_by_id(id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            'DELETE FROM todos WHERE id = ?',
            (id,)
        )

        if cursor.rowcount == 0:
            return False

    return True

def update_todo_by_id(id, data):
    fields = []
    values = []

    if "title" in data:
        fields.append("title = ?")
        values.append(data["title"])

    if "completed" in data:
        fields.append("completed = ?")
        values.append(data["completed"])

    if not fields:
        return False

    values.append(id)

    query = f"""
        UPDATE todos
        SET {", ".join(fields)}
        WHERE id = ?
    """

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(query, values)

        return cursor.rowcount > 0