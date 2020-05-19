# Using Scripts to Automate Data Entry

## Background

Bundled with this assignment is a simple, incomplete command-line tool for entering data into a database.
The file `insert.py` allows the user two different methods for adding data to a given database.

**Usage:**
`python3 insert.py [-h] [-r ROSTER] db`

- **`-h`** brings up help text
- **`-r ROSTER`** adds names from the file `ROSTER`. `ROSTER` is assumed to be a plain-text file with one name per line. 
Without this option names are entered through an interactive prompt.
- **`db`** the path of the sqlite database to be edited

**Examples:**

**`python3 insert.py test.sqlite`** - starts an interactive prompt which allows the user to add names to the `test.sqlite` database

**`python3 insert.py -r roster.txt test.sqlite`** - inserts the names from `roster.txt` to the `test.sqlite` database

## Instructions

1. Use the `insert.py` CLI as described above to enter a few names into the `nbtt.sqlite` database by hand.
2. Use a SQLite CLI(`sqlite3`, `litecli`, etc.) to open the database you just edited and run a query to ensure the
data was added to the database.
3. Use the `insert.py` CLI as described above to add the roster `roster2019-20.txt` to the `nbtt.sqlite` database.
4. Repeat step 2.
5. Use the `insert.py` CLI as described above to add the roster `roster2020-21.txt` to the `nbtt.sqlite` database.
6. Repeat step 2. What's changed? Why did this happen?
7. Rewrite `insert.py` to protect it from injection attacks.

## Docs & Resources

- [SQL SELECT Statement](https://www.w3schools.com/sql/sql_select.asp)
- [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3)
- [Robert Tables](https://xkcd.com/327/)

## Bailing Out

To reset the state of the database to its original form, run the following command in your working directory:
`cp .nbtt.bak nbtt.sqlite`

To reset the state of `insert.py` to its original form, run the following command in your working directory:
`cp .insert.py.bak insert.py`

Why aren't you using `git`?
