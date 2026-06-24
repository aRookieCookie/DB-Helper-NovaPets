BEGIN TRANSACTION;
DROP TABLE IF EXISTS "inventory";
CREATE TABLE "inventory" (
	"ID"	INTEGER,
	"player_id"	INTEGER,
	"item_id"	INTEGER,
	"quantity"	INTEGER,
	"obtained_on"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("item_id") REFERENCES "items"("ID"),
	FOREIGN KEY("player_id") REFERENCES "users"("ID")
);
DROP TABLE IF EXISTS "items";
CREATE TABLE "items" (
	"ID"	INTEGER,
	"naam"	TEXT,
	"type"	TEXT,
	"health_effect"	INTEGER,
	"hunger_effect"	INTEGER,
	"dorst_effect"	INTEGER,
	"description"	INTEGER,
	"cost"	INTEGER DEFAULT 0,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "pets";
CREATE TABLE "pets" (
	"ID"	INTEGER,
	"owner_id"	INTEGER,
	"docent_id"	INTEGER,
	"health"	INTEGER,
	"thirst"	INTEGER,
	"hunger"	INTEGER,
	"temp"	REAL,
	"age"	INTEGER,
	"mood"	INTEGER,
	"last_seen"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("docent_id") REFERENCES "",
	FOREIGN KEY("owner_id") REFERENCES "users"("ID")
);
DROP TABLE IF EXISTS "stats";
CREATE TABLE "stats" (
	"ID"	INTEGER,
	"naam"	TEXT,
	"max_health"	INTEGER,
	"fortitude_multi"	REAL,
	"mood_multi"	REAL,
	"thirst_multi"	REAL,
	"hunger_multi"	REAL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "users";
CREATE TABLE "users" (
	"ID"	INTEGER,
	"username"	TEXT UNIQUE,
	"password_hash"	TEXT,
	"created_at"	TEXT,
	"coins"	INTEGER DEFAULT 0,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
COMMIT;
