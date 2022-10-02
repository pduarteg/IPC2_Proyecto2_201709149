class Empresa:
	
	next = None
	
	def __init__(self, id, name, abbreviation, point_list, transaction_list):
		self.id = id
		self.name = name
		self.abbreviation = abbreviation
		self.point_list = point_list
		self.transaction_list = transaction_list

	def imprimir_datos_de_empresa(self):
		print("---------------------------------------------------------------------")
		print(" Id: " + self.id)
		print(" Nombre: " + self.name)		
		print(" Abreviatura:" + self.abbreviation)
		print("---------------------------------------------------------------------")