import db
import re

def add_vote(message):
	abbrev, vote = parse_mesg(message)
	d = {'vote': vote, 'abbrev': abbrev}
	db.upd_db(d)

def ch_num_people():
	hp, vote = parse_mesg(message)
	d = {'house_population': hp, 'abbrev': abbrev}
	db.upd_db(d)

def parse_mesg(message):
	result = re.search(r'/v (.+) (.+)', message)
	return result.group(1), result.group(2)
	

def stat_house():
	pass

def stat_uik():
	pass

# if __name__ == "__main__":
# 	add_vote('/v K9 2')