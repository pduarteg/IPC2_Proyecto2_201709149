class Escritorio:

	state = False
	next = None
	
	def __init__(self, id, identification, manager):
		self.id = id
		self.identification = identification
		self.manager = manager