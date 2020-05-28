import sqlite3

# This is based on the sqlite3 documentation
conn = sqlite3.connect("corrupt.sqlite")
c = conn.cursor()

# Start editing below


def delete_track(title):
    """
    Deletes songs named <title> from the track table
    of the connected database. Should return None if successful
    """
    query = "DELETE FROM track WHERE name=?"
    c.execute(query, (title,))

delete_track("Blame It on the Rain")
conn.commit()
conn.close()
