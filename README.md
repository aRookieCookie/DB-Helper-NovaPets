[![Banner](site/banner.jpg)](https://arookiecookie.github.io/DB-Helper-NovaPets/site/)
# 📖 Inhoudsopgave

* [⬇️ Install Process](#-install-process)
* [📊 Database Structure](#-database-structure)
* [</> Functions](#-functions)

# ⬇️ Install Process

1. Download de Laatste Release ZIP file.
2. Extract de folder naar dezelfde map waar de *main* file zich bevind.
3. Run de `create_schema.sql` als de `nova_pets.db` faalt
4. Zorg dat de dir er zo uitziet
```
project_root/
│
├── main.py
├── nova_pets.db
│
├── db_handler/
│   ├── __init__.py
│   ├── connection.py
│   ├── syslog.py
│   │
│   ├── models/
│       ├── __init__.py
│       ├── pet.py
│       ├── user.py
│       └── etc...
|
└── requirements.txt
```
6. Voeg deze lijn toe:
```python
from db_handler.models import user, pets, inventory, items, variants
```
4. Done. probeer bijvoorbeeld:
```python
from db_handler.models import user, pets, inventory, items, variants

pet = pets.get_by_id(                               # Krijg de pet class met de data die nodig is voor het verwijderen
          pets.create_pet(owner_id=1, docent_id=1)) # Instantiate een nieuwe pet, de functie returns de id. de ID is vereist voor de data.
          .kill()                                   # Vermoord de pet direct
```
> Deze code maakt een pet aan, vind de pet, vermoord de pet. De database veranderd hierdoor uiteindelijk niet.

---

# 📊 Database Structure

### Players
| Column | Type | Description |
|--------|------|-------------|
| ID | INTEGER PRIMARY KEY | Unieke speler identificatie |
| username | TEXT UNIQUE | Gebruikersnaam |
| password_hash | TEXT | Gehashte wachtwoord |
| created_at | TEXT | Account aanmaak datum |

**Type:** Dynamisch

-

### Pets
| Column | Type | Description |
|--------|------|-------------|
| ID | INTEGER PRIMARY KEY | Unieke pet identificatie |
| owner_id | INTEGER | Verwijzing naar players.ID |
| docent_id | INTEGER | Verwijzing naar stats.ID (pet variant) |
| health | INTEGER | Huidige gezondheid |
| dorst | INTEGER | Dorst niveau (0-100) |
| honger | INTEGER | Honger niveau (0-100) |
| temp | REAL | Temperatuur |
| age | INTEGER | Leeftijd |
| last_seen | TEXT | Laatst gezien timestamp |

**Type:** Dynamisch

-

### Stats
| Column | Type | Description |
|--------|------|-------------|
| ID | INTEGER PRIMARY KEY | Unieke stat identificatie |
| naam | TEXT | Naam van de docent/variant |
| max_health | REAL | Maximum gezondheid |
| fortitude_multi | REAL | Fortitude multiplier |
| mood_multi | REAL | Mood multiplier |
| thurst_multi | REAL | Dorst multiplier |
| hunger_multi | REAL | Honger multiplier |

**Type:** Statisch (base stats voor pet varianten)

-

### Items
| Column | Type | Description |
|--------|------|-------------|
| ID | INTEGER PRIMARY KEY | Unieke item identificatie |
| naam | TEXT | Naam van het item |
| type | TEXT | Item categorie (food, drink, potion, etc.) |
| health_effect | INTEGER | Effect op gezondheid |
| hunger_effect | INTEGER | Effect op honger |
| dorst_effect | INTEGER | Effect op dorst |

**Type:** Statisch (item definities)

-

### Inventory
| Column | Type | Description |
|--------|------|-------------|
| ID | INTEGER PRIMARY KEY | Unieke inventory entry |
| player_id | INTEGER | Verwijzing naar players.ID |
| item_id | INTEGER | Verwijzing naar items.ID |
| quantity | INTEGER | Aantal items |
| obtained_on | TEXT | Verkrijg datum |

**Type:** Dynamisch

---

# </> Functions
### User<sup><sub>⌛</sup></sub>: 
- [ ] Create  
- [ ] Delete  
- [ ] Verify  
- [ ] Change Password

### Pets:
- [ ] Create
- [ ] Get Status
- [ ] Set Status
- [ ] Delete
- [ ] Get All

### Variants
- [ ] Create
- [ ] Get Stats
- [ ] Delete

### Inventory
- [ ] Get
- [ ] Add Item
- [ ] Edit Quantity
- [ ] Remove Item

### Items
- [ ] Create
- [ ] Delete
- [ ] Get
- [ ] Edit
