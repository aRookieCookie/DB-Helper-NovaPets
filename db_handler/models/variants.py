from db_handler.connection import get_connection

def create(naam, max_health, fortitude_multi, mood_multi, thirst_multi, hunger_multi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO stats (naam, max_health, fortitude_multi, mood_multi, thirst_multi, hunger_multi)
                   VALUES (?, ?, ?, ?, ?, ?)
                   """, (naam, max_health, fortitude_multi, mood_multi,thirst_multi, hunger_multi))
    varient_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return varient_id

def get_stats(docent_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stats WHERE id = ?", (docent_id,))
    row = cursor.fetchone()

    return {
        "naam" : row["naam"],
        "max_health" : row["max_health"],
        "fortitude" : row["fortitude_multi"],
        "mood" : row["mood_multi"],
        "thirst" : row["thirst_multi"],
        "hunger" : row["hunger_multi"]
    }

def delete(docent_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stats WHERE id = ?", (docent_id,))
    conn.commit()
    conn.close()