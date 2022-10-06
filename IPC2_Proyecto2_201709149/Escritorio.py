class Escritorio:

	state = False
	next = None

	# sim values
	total_a_time = 0
	med_time = 0
	min_a_time = None
	max_a_time = None
	a_client = None
	total_clients_a = 0
	
	def __init__(self, id, identification, manager):
		self.id = id
		self.identification = identification
		self.manager = manager

	def set_state(self, value):
		self.state = value

	def reset_sim_values(self):
		self.total_a_time = 0
		self.med_time = 0
		self.min_a_time = 0
		self.max_a_time = 0
		self.a_client = None
		self.total_clients_a = 0

	def print_desk_state(self):
		print("     ID: " + self.id)
		print("       Identificación: " + self.identification)
		print("       Encargado: " + self.manager)
		if self.a_client != None:
			print("       Cliente en atención previa: " + self.a_client.name)
		if self.total_clients_a > 0:
			print("       Tiempo promedio de atención: " + str(self.med_time) + " minutos.")
			print("       Tiempo máximo de atención: " + str(self.max_a_time) + " minutos.")
			print("       Tiempo mínimo de atención: " + str(self.min_a_time) + " minutos.")
			print("       Cantidad de clientes atendidos por este escritorio: " + str(self.total_clients_a))
		else:
			print("       Este escritorio aún no ha atendido clientes.")

	def round_values(self):
		self.med_time = round(self.med_time, 2)
		self.min_a_time = round(self.min_a_time, 2)
		self.max_a_time = round(self.max_a_time, 2)