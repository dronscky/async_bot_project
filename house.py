class House:
'''address, abbrev, vote, house_population, uik_population'''
	def __init__(self, abbrev):
		self.abbrev = abbrev
		self._houses = self._load_houses()

	def _load_houses():
		pass