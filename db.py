import sqlite3

def db(func):
	def wrapper(*args, **kwargs):
		conn = sqlite3.connect('mydb.db')
		cursor = conn.cursor()
		cursor.execute(func(*args, **kwargs))
		print(cursor.fetchall())
		conn.commit()
	return wrapper

### Insert new data
# sql = """INSERT INTO U275 (address, abbrev, vote, house_population, uik_population)
# 	VALUES (
# 	'Академика Королева 9',
# 	'K9',
# 	5,
# 	150,
# 	900
# 	)"""


### Update field
# sql = """UPDATE U275 SET vote=7 WHERE abbrev='K9'"""

### Select data
# sql = """SELECT vote FROM U275 WHERE abbrev='K9'"""

#### Create new TABLE

# sql = """CREATE TABLE U275 
# 	(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
# 	address TEXT,
# 	abbrev CHAR(5),
# 	vote INTEGER,
# 	house_population INTEGER,
# 	uik_population INTEGER,
# 	UNIQUE(address, abbrev)
# 	) 
# 	"""

@db
def request(abbrev):
	sql = """SELECT vote FROM U275 WHERE abbrev='%s'"""%(abbrev)
	return sql

request('K9')
