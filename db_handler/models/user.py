from db_handler.connection import get_connection
import bcrypt
import datetime

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


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def delete(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return True

def verify_password(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return False

    stored_hash = row[0]
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

def change_password(user_id, new_password):
    conn = get_connection()
    cursor = conn.cursor()
    new_hash = hash_password(new_password)
    cursor.execute("UPDATE users SET password_hash = ? WHERE id = ?", (new_hash, user_id))
    conn.commit()
    conn.close()
    return True
