class Punto:
	
	next = None
	
	def __init__(self, id, name, adress, desk_list):
		self.id = id
		self.name = name
		self.adress = adress
		self.desk_list = desk_list

	def imprimir_datos_de_punto(self):
		print("---------------------------------------------------------------------")
		print(" Id: " + self.id)
		print(" Nombre: " + self.name)		
		print(" Dirección:" + self.adress)
		print("---------------------------------------------------------------------")