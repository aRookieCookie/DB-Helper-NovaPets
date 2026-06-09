from db_handler.connection import get_connection

def create(naam, max_health, fortitude_multi, mood_multi, thirst_multi, hunger_multi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO stats (naam, max_health, fortitude_multi, mood_multi, thirst_multi, hunger_multi)
                   VALUES (?, ?, ?, ?, ?, ?)
                   """, (naam, max_health, fortitude_multi, mood_multi,thirst_multi, hunger_multi))
    varient_id = pet_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return varient_id