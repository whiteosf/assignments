import sqlite3
import argparse

# Setup for CLI. Do not touch!
# ===== BEGIN CLI BLOCK ===== #

parser = argparse.ArgumentParser()
parser.add_argument("db", default=":memory:", help="The file path of the database to be edited")
parser.add_argument("-r", "--roster", help="Inserts names from ROSTER into db. ROSTER should be a plain-text file with one name on each line.")
args = parser.parse_args()

# ===== END CLI BLOCK ===== #

conn = sqlite3.connect(args.db)
cur = conn.cursor()

if args.roster:
    with open(args.roster) as f:
        for record in f:
            name = record.strip()
<<<<<<< HEAD
            cur.executescript(f"INSERT INTO students (name) values ('{name}')")
=======
            cur.execute("INSERT INTO students (name) VALUES (?)", (name,))
>>>>>>> a67e48a602b8a5566681ae4fdf897b0872958a0d
            conn.commit()
        conn.close()

else:
    while True:
        name = input("Type your first and last name and hit enter to register. Hit Ctrl+C to quit.\n> ")
<<<<<<< HEAD
        cur.execute(f"INSERT INTO students (name) VALUES ('{name}');")
=======
        cur.execute("INSERT INTO students (name) VALUES (?)", (name,))
>>>>>>> a67e48a602b8a5566681ae4fdf897b0872958a0d
        conn.commit()

