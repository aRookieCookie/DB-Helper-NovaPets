BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "inventory" (
	"ID"	INTEGER,
	"player_id"	INTEGER,
	"item_id"	INTEGER,
	"quantity"	INTEGER,
	"obtained_on"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("item_id") REFERENCES "items"("ID"),
	FOREIGN KEY("player_id") REFERENCES "users"("ID")
);
CREATE TABLE IF NOT EXISTS "items" (
	"ID"	INTEGER,
	"naam"	TEXT,
	"type"	TEXT,
	"health_effect"	INTEGER,
	"hunger_effect"	INTEGER,
	"dorst_effect"	INTEGER,
	"description"	INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "pets" (
	"ID"	INTEGER,
	"owner_id"	INTEGER,
	"docent_id"	INTEGER,
	"health"	INTEGER,
	"thirst"	INTEGER,
	"hunger"	INTEGER,
	"temp"	REAL,
	"age"	INTEGER,
	"last_seen"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("docent_id") REFERENCES "",
	FOREIGN KEY("owner_id") REFERENCES "users"("ID")
);
CREATE TABLE IF NOT EXISTS "stats" (
	"ID"	INTEGER,
	"naam"	TEXT,
	"max_health"	INTEGER,
	"fortitude_multi"	REAL,
	"mood_multi"	REAL,
	"thurst_multi"	REAL,
	"hunger_multi"	REAL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users" (
	"ID"	INTEGER,
	"username"	TEXT UNIQUE,
	"password_hash"	TEXT,
	"created_at"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
COMMIT;
