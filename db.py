import sqlite3
import os
from config import PATH


conn = sqlite3.connect(os.path.join(PATH, 'mydb.db'))
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
	if values[1] != 'D':
		sql = f"UPDATE U275 SET {columns[0]}='{values[0]}' WHERE {columns[1]}='{values[1]}'"
	else: 
		sql = f"UPDATE U275 SET vote='{values[0]}', house_population='{values[0]}' WHERE {columns[1]}='{values[1]}'"
	cursor.execute(sql)	
	conn.commit()

'''
col is vote or house_population
'''
def sum(col):
	sql = f"SELECT SUM({col}) FROM U275"
	cursor.execute(sql)
	return cursor.fetchone()[0]

def get_house_info(col, abbrev):
	sql = f"SELECT {col} FROM U275 WHERE abbrev='{abbrev}'"
	cursor.execute(sql)
	return cursor.fetchone()[0]

"""пример реализации с декоратором"""
# def db(func):
# 	def wrapper(*args, **kwargs):
# 		conn = sqlite3.connect('mydb.db')
# 		cursor = conn.cursor()
# 		cursor.execute(func(*args, **kwargs))
# 		print(cursor.fetchall())
# 		conn.commit()
# 	return wrapper

def selectdb():
	sql = f"SELECT * FROM U275"
	cursor.execute(sql)
	print(cursor.fetchall())

#### Test summary report

def report_voting():
	sql = f"SELECT address, vote, house_population FROM U275"
	cursor.execute(sql)
	res = cursor.fetchall()
	return res

def show_report():
	data = report_voting()
	s = ''
	for i in data:
		s = s + f'{i[0]} проголосовало {i[1]} из {i[2]} \n'
	v = sum('vote')
	hp = sum('house_population')
	s = s + f'Всего проголосовало {str(v)} из {str(hp)} ({round(v/hp*100, 2)}%)'	
	return s
####

if __name__ == '__main__':
	# _init_db()
	selectdb()
	# sum('house_population')

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


