from db_handler.connection import get_connection
import datetime

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

import datetime

def buy(item_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()

    # krijg de item cost
    cursor.execute("SELECT cost FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()

    if row is None:
        print("Item niet gevonden.")
        cursor.close()
        conn.close()
        return False

    cost = row[0]

    cursor.execute(
        "UPDATE users SET coins = coins - ? WHERE id = ? AND coins >= ?", 
        (cost, user_id, cost)
    )

    # Check of aankoop is mislukt
    if cursor.rowcount == 0:
        print("Aankoop mislukt: te weinig coins of gebruiker bestaat niet.")
        cursor.close()
        conn.close()
        return False

    # 3. ITEM GEVEN: Controleer of het item al in de inventaris staat van deze speler
    cursor.execute(
        "SELECT quantity FROM inventory WHERE player_id = ? AND item_id = ?", 
        (user_id, item_id)
    )
    inv_row = cursor.fetchone()

    huidige_tijd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if inv_row:
        # Item bestaat al -> Verhoog de 'quantity' met 1 en update eventueel de datum
        cursor.execute(
            "UPDATE inventory SET quantity = quantity + 1, obtained_on = ? WHERE player_id = ? AND item_id = ?",
            (huidige_tijd, user_id, item_id)
        )
    else:
        # Item bestaat nog niet -> Voeg een nieuwe rij toe met quantity = 1
        cursor.execute(
            "INSERT INTO inventory (player_id, item_id, quantity, obtained_on) VALUES (?, ?, ?, ?)",
            (user_id, item_id, 1, huidige_tijd)
        )

    # 4. Sla ALLES definitief op!
    conn.commit()
    print("Aankoop succesvol en item is toegevoegd aan de inventory!")

    cursor.close()
    conn.close()
    return True