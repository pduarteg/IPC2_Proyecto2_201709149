class Cliente:

	next = None
	
	def __init__(self, dpi, name, transactions_list):
		self.dpi = dpi
		self.name = name
		self.transactions_list = transactions_list