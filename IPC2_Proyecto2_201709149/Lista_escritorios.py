import Escritorio

class Lista_escritorios:

	first = None
	cant = 0
	active_n = 0
	unactive_n = 0

	def add(self, escritorio):
		if self.first == None:
			self.first = escritorio
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = escritorio
			self.cant += 1

	def mostrar_escritorios(self):
		temp = self.first
		
		while temp != None:
			temp.imprimir_datos_de_escritorio()
			temp = temp.next

	def buscar_por_nombre(self, name):
		r_escritorio = None
		temp = self.first

		while temp != None:
			if temp.name == name:
				r_escritorio = temp
				break
			else:
				temp = temp.next

		return r_escritorio

	def buscar_por_posicion(self, pos):
		actual = self.first
		for i in range(pos-1):
			actual = actual.next
		return actual

	def buscar_inactivo(self, pos):
		n = 0
		temp = self.first

		while temp != None:
			if temp.state == False:
				n += 1
			if n == pos:
				break
			temp = temp.next
		return temp

	def buscar_activo(self, pos):
		n = 0
		temp = self.first

		while temp != None:
			if temp.state == True:
				n += 1
			if n == pos:
				break
			temp = temp.next
		return temp

	def buscar_por_id(self, id):
		temp = self.first

		while temp != None:
			if temp.id == id:
				break
			temp = temp.next
		return temp

	def mostrar_activos(self):
		n = 1
		temp = self.first

		while temp != None:
			if temp.state:
				print(" [" + str(n) + "] " + temp.id)
				n += 1
			temp = temp.next        	
		print(" [0] Volver sin seleccionar")

	def mostrar_inactivos(self):
		n = 1
		temp = self.first

		while temp != None:
			if temp.state == False:
				print(" [" + str(n) + "] " + temp.id)
				n += 1
			temp = temp.next        	
		print(" [0] Volver sin seleccionar")

	def contar_todos(self):
		self.active_n = 0
		self.unactive_n = 0
		temp = self.first
		while temp != None:
			if temp.state:
				self.active_n += 1
			else:
				self.unactive_n += 1
			temp = temp.next