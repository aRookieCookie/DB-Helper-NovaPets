from db_handler.connection import get_connection

# CLASS TO STORE/MODIFY PET DATA
class Pet:
    # STORE ALL DATA IN THE CLASS
    def __init__(self, id, owner_id, docent_id, health, thirst, hunger, temp, age, mood, last_seen, naam, max_health, fortitude_multiplier, mood_multiplier, thirst_multiplier, hunger_multiplier):
        self.id = id
        self.owner_id = owner_id
        self.docent_id = docent_id
        self.health = health
        self.thirst = thirst
        self.hunger = hunger
        self.temp = temp
        self.age = age
        self.mood = mood
        self.last_seen = last_seen
        self.naam = naam
        self.max_health = max_health
        self.fortitude_multiplier = fortitude_multiplier
        self.mood_multiplier = mood_multiplier
        self.thirst_multiplier = thirst_multiplier
        self.hunger_multiplier = hunger_multiplier

    #KILL PET
    def kill(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pets WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

def create(owner_id, docent_id, temp=20.5):
    conn = get_connection()
    cursor = conn.cursor()
    default_stats = look_up_stats(docent_id)
    cursor.execute("""
                   INSERT INTO pets (owner_id, docent_id, health, thirst, hunger, temp, age, mood, last_seen)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                   """, (owner_id, docent_id, default_stats["max_health"], 100, 100, temp, 0, 100, 0))
    pet_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return pet_id

# GET PET DATA BY ID
def get_by_id(pet_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT * FROM pets
                   INNER JOIN stats ON pets.docent_id = stats.id
                   WHERE pets.id = ?
                   """, (pet_id,))
    row = cursor.fetchone()
    conn.close()

    # CHECK IF PET EXISTS
    if row is None:
        return None
    
    # CREATE PET OBJECT WITH THE DATA FROM THE DATABASE
    return Pet(
            id=row["id"],
            owner_id=row["owner_id"],
            docent_id=row["docent_id"],
            health=row["health"],
            thirst=row["thirst"],
            hunger=row["hunger"],
            temp=row["temp"],
            age=row["age"],
            mood=row["mood"],
            last_seen=row["last_seen"],
            naam=row["naam"],
            max_health=row["max_health"],
            fortitude_multiplier=row["fortitude_multi"],
            mood_multiplier=row["mood_multi"],
            thirst_multiplier=row["thirst_multi"],
            hunger_multiplier=row["hunger_multi"]
        )

def look_up_stats(docent_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stats WHERE id = ?", (docent_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "naam": row["naam"],
        "max_health": row["max_health"],
        "fortitude_multi": row["fortitude_multi"],
        "thirst_multi": row["thirst_multi"],
        "hunger_multi": row["hunger_multi"],
        "mood_multi": row["mood_multi"]
    }

def get_all(owner_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID FROM pets WHERE owner_id = ?", (owner_id,))
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pets WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return True

def set_status(
    id,
    owner_id=None,
    docent_id=None,
    health=None,
    thirst=None,
    hunger=None,
    temp=None,
    age=None,
    mood=None,
    last_seen=None,
    naam=None
):
    fields = {
        "docent_id": docent_id,
        "health": health,
        "thirst": thirst,
        "hunger": hunger,
        "temp": temp,
        "age": age,
        "mood": mood,
        "last_seen": last_seen,
        "naam": naam
    }

    updates = []
    values = []

    for column, value in fields.items():
        if value is not None:
            updates.append(f"{column} = ?")
            values.append(value)

    if not updates:
        return False

    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
        UPDATE pets
        SET {", ".join(updates)}
        WHERE ID = ?
    """

    values.append(id)

    cursor.execute(query, values)

    conn.commit()
    conn.close()

    return True

    