from db_handler.connection import get_connection
import bcrypt
import datetime

class User:
    def __init__(self, id, username, password, created_at):
        self.id = id
        self.username = username
        self.password = password
        self.created_at = created_at

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    conn.close()
    return cursor.fetchall()

def create(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)", (username, hash_password(password), datetime.datetime.now().isoformat()))
    conn.commit()
    id = cursor.lastrowid
    conn.close()

    return id

def get(query):
    conn = get_connection()
    cursor = conn.cursor()
    if isinstance(query, int):
        cursor.execute("SELECT * FROM users WHERE id = ?", (query,))
    else:
        cursor.execute("SELECT * FROM users WHERE username = ?", (query,))
    row = cursor.fetchone()
    print(row)
    user = User(row[0], row[1], row[2], row[3]) if row else None
    conn.close()
    return user


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def delete(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return True

def verify(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return False

    user_id, stored_hash = row
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return user_id
    else:
        return False

def change_password(user_id, new_password):
    conn = get_connection()
    cursor = conn.cursor()
    new_hash = hash_password(new_password)
    cursor.execute("UPDATE users SET password_hash = ? WHERE id = ?", (new_hash, user_id))
    conn.commit()
    conn.close()
    return True
