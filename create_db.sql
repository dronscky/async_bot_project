create table u275 (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	address TEXT,
	abbrev CHAR(5),
	vote INTEGER,
	house_population INTEGER,
	UNIQUE(address, abbrev)
	);

insert into u275 (address, abbrev, vote, house_population)
values
	('Ак. Королева, 9', 'К9', 0, 100),
	('Ак. Королева, 15', 'К15', 0, 100),
	('Ак. Королева, 17', 'К17', 0, 100),
	('Ак. Королева, 19', 'К19', 0, 100),
	('Ак. Королева, 21', 'К21', 0, 100),
	('Дополнительный список', 'Д', 0, 0);