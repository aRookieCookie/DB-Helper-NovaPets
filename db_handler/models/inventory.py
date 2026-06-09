from db_handler.connection import get_connection

def get(player_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT player_id, item_id, quantity FROM inventory WHERE player_id = ?", (player_id,))
    rows = cursor.fetchall()
    player_inventory = [dict(row) for row in rows]
    conn.close()
    return player_inventory

def add(player_id, item_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO inventory (player_id, item_id, quantity, obtained_on)
        VALUES (?, ?, ?, '00:00')
        ON CONFLICT(player_id, item_id) 
        DO UPDATE SET quantity = quantity + excluded.quantity
    """, (player_id, item_id, quantity))
    
    conn.commit()
    conn.close()
    return True

def set_quantity(player_id, item_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE inventory 
        SET quantity = ? 
        WHERE player_id = ? AND item_id = ?
    """, (quantity, player_id, item_id))
    
    conn.commit()
    conn.close()
    return True

def remove(player_id, item_id, quantity_to_remove):
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Deduct the quantity from the player's item
    cursor.execute("""
        UPDATE inventory 
        SET quantity = quantity - ? 
        WHERE player_id = ? AND item_id = ?
    """, (quantity_to_remove, player_id, item_id))
    
    # 2. Safety check: If the item count dropped to 0 (or below), delete the row entirely
    cursor.execute("""
        DELETE FROM inventory 
        WHERE player_id = ? AND item_id = ? AND quantity <= 0
    """, (player_id, item_id))
    
    conn.commit()
    conn.close()
    return True