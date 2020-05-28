import sqlite3

# Write a script below that connects to the chinook.sqlite
# database in this directory and adds your favorite song and
# all its related data to the track table.

conn = sqlite3.connect("chinook.sqlite")
c = conn.cursor()

# You can use:
# pragma table_info(track);
# from a SQL prompt to get column info about the track table
#
# from there we see that we only have to fill in the track's
# name, mediatypeid, milliseconds, and unitprice
# the trackid is the primary key so it'll be assigned automatically
# if we omit it

query = ("INSERT INTO track (name, mediatypeid, milliseconds, unitprice) "
         "VALUES ('Gravity', 2, 233000, .99) ")

c.execute(query)
conn.commit()
conn.close()
