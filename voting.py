import db
import re

def add_vote(message):
	if parse_mesg(message) != 'Error data':
		abbrev, vote = parse_mesg(message)
		d = {'vote': vote, 'abbrev': abbrev}
		db.upd_db(d)
		res = []
		res.append(get_address_house(abbrev))
		res.append(calc_stat_house(vote, abbrev))
		res.append(calc_stat_uik())
		return res
	else:
		return 'Error'	

def ch_num_people(message):
	if parse_mesg(message) != 'Error data':
		abbrev, hp = parse_mesg(message)
		d = {'house_population': hp, 'abbrev': abbrev}
		db.upd_db(d)
	else:
		return  "Error"	

def parse_mesg(message):
	result = re.search(r'/v (.+) (.+)', message)
	if re.search(r'K9|K15|K17|K19|K21|D', result.group(1)) and re.search(r'\d+', result.group(2)):
		return result.group(1), result.group(2)
	else:
		return 'Error data'

def get_address_house(abbrev):
	return db.get_house_info('address', abbrev)

def calc_stat_house(n, abbrev):
	return round(int(n)/db.get_house_info('house_population', abbrev)*100, 1)

def calc_stat_uik():
	return round(db.sum('vote')/db.sum('house_population')*100, 1)

# if __name__ == "__main__":
# 	add_vote('/v K9 2')