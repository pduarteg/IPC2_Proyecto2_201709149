class Transaccion:

	next = None

	def __init__(self, id, name, a_time, cant):
		self.id = id
		self.name = name
		self.a_time = a_time
		self.cant = cant