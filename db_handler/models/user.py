from db_handler.connection import get_connection
import bcrypt
import datetime

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    conn.close()
    return cursor.fetchall()

def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)", (username, hash_password(password), datetime.datetime.now().isoformat()))
    conn.commit()
    conn.close()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

