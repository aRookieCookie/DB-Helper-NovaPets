from db_handler.connection import get_connection

def create(naam, type, health_effect, hunger_effect, dorst_effect, description, cost):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO stats (naam, type, health_effect, hunger_effect, dorst_effect, description)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   """, (naam, type, health_effect, hunger_effect, dorst_effect, description, cost))
    item_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return item_id

def delete(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

def get(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()

    return {
        "naam" : row["naam"],
        "type" : row["type"],
        "health_effect" : row["health_effect"],
        "hunger_effect" : row["hunger_effect"],
        "dorst_effect" : row["dorst_effect"],
        "description" : row["description"],
        "cost" : row["cost"]
    } 

def edit(item_id, name, value):
    conn = get_connection()
    cursor = conn.cursor()
    
    if name in ["naam", "type", "health_effect", "hunger_effect", "dorst_effect", "description", "cost"]:
            cursor.execute(f"UPDATE items SET ? = ? WHERE id = ?", (name, value, item_id))
            conn.commit()
            conn.close()
            return True
    else:
        print("Variable name not in table")

def buy(item_id, user_id):
    conn = get_connection
    cursor = conn.cursor()

    cursor.execute("SELECT cost FROM items WHERE id = ?)", (item_id))
    cost = cursor.fetchone()

    if cost:
        cursor.execute(
        "UPDATE users SET coins = coins - ? WHERE id = ? AND coins >= ?", 
        (cost, user_id, cost)
    )
        cursor.close()
        conn.close()
        print(f"User({user_id}) Bought a item({item_id}) for {cost}")
    else:
        print("cost not found")
        cursor.close()
        conn.close()
