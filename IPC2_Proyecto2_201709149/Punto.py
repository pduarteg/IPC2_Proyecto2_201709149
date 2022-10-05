class Punto:
	
	next = None
	med_wait_time = 0
	max_wait_time = 0
	min_wait_time = 0
	med_a_time = 0
	max_a_time = 0
	min_a_time = 0
	
	def __init__(self, id, name, adress, desk_list):
		self.id = id
		self.name = name
		self.adress = adress
		self.desk_list = desk_list

	def imprimir_datos_de_punto(self):
		print("---------------------------------------------------------------------------")
		print(" Id: " + self.id)
		print(" Nombre: " + self.name)		
		print(" Dirección:" + self.adress)
		print("---------------------------------------------------------------------------")

	def reset_sim_data(self):
		self.med_wait_time = 0
		self.max_wait_time = 0
		self.min_wait_time = 0
		self.med_a_time = 0
		self.max_a_time = 0
		self.min_a_time = 0
		temp = self.desk_list.first

		while temp != None:
			temp.reset_sim_values()
			temp = temp.next