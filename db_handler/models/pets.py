from db_handler.connection import get_connection
from db_handler import syslog as log

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
        print(log.SUCCESS_DATA_DELETED)

def create_pet(owner_id, docent_id, temp=20.5):
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
    print(log.SUCCESS_DATA_CREATED)
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
        print(log.ERROR_DATA_NOT_FOUND)
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
        print(log.ERROR_DATA_NOT_FOUND)
        return None

    return {
        "naam": row["naam"],
        "max_health": row["max_health"],
        "fortitude_multi": row["fortitude_multi"],
        "thirst_multi": row["thirst_multi"],
        "hunger_multi": row["hunger_multi"],
        "mood_multi": row["mood_multi"]
    }