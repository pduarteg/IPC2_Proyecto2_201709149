class Configuracion:

	next = None

	def __init__(self, id, idCompany, idPoint, active_desk_list, client_list):
		self.id = id
		self.idCompany = idCompany
		self.idPoint = idPoint
		self.active_desk_list = active_desk_list
		self.client_list = client_list