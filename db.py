import sqlite3

conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

def _init_db():
	with open('create_db.sql', 'r') as f:
		sql = f.read()
	cursor.executescript(sql)
	conn.commit()

def get_cursor():
	return cursor



'''
Dictionary must be {'vote': '', 'abbrev': ''} 
or {'house_population':, 'abbrev': ''}
'''
def upd_db(d):
	columns = [*d.keys()]
	values = [*d.values()]
	sql = f"UPDATE U275 SET {columns[0]}='{values[0]}' WHERE {columns[1]}='{values[1]}'"
	cursor.execute(sql)
	conn.commit()

"""пример реализации с декоратором"""
# def db(func):
# 	def wrapper(*args, **kwargs):
# 		conn = sqlite3.connect('mydb.db')
# 		cursor = conn.cursor()
# 		cursor.execute(func(*args, **kwargs))
# 		print(cursor.fetchall())
# 		conn.commit()
# 	return wrapper

def insert_db():
	sql = f""

def selectdb():
	sql = f"SELECT * FROM U275 WHERE abbrev='K19'"
	cursor.execute(sql)
	print(cursor.fetchall())

if __name__ == '__main__':
	# _init_db()
	selectdb()


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

# def init_db():
	# sql = """CREATE TABLE U275 
	# 	(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	# 	address TEXT,
	# 	abbrev CHAR(5),
	# 	vote INTEGER,
	# 	house_population INTEGER,
	# 	uik_population INTEGER,
	# 	UNIQUE(address, abbrev)
	# 	) 
	# """


