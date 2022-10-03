class Configuracion:

	next = None

	def __init__(self, id, idCompany, idPoint, active_desk_list, client_list):
		self.id = id
		self.idCompany = idCompany
		self.idPoint = idPoint
		self.active_desk_list = active_desk_list
		self.client_list = client_list

	def apply(self, data):
		print("")
		print(" *** Aplicando congiruación: " + self.id)		
		print(" *** Buscando empresa...")
		if data != None:
			company = data.buscar_por_id(self.idCompany)

			if company != None:
				print(" *** Buscando punto...")
				point = company.point_list.buscar_por_id(self.idPoint)
				if point != None:
					print(" *** Configurando escritorios...")
					temp_desk = self.active_desk_list.first

					while temp_desk != None:
						found_desk = point.desk_list.buscar_por_id(temp_desk.id)
						if found_desk != None:
							# Activa el escritorio encontrado
							found_desk.set_state(True)
						else:
							print(" (!) No se ha encontrado el escritorio: " + temp_desk.id + " para configurar.")
						temp_desk = temp_desk.next
					print(" *** Escritorios configurados.")
				else:
					print(" (!) No se ha encontrado el punto para configurar.")
			else:			
				print(" (!) No se ha encontrado la empresa para configurar.")
		else:
			print(" (!) No hay datos en memoria.")