import Configuracion

class Lista_configuraciones:

	first = None
	cant = 0

	def add(self, configuracion):
		if self.first == None:
			self.first = configuracion
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = configuracion
			self.cant += 1

	def mostrar_configuracions(self):
		temp = self.first
		
		while temp != None:
			temp.imprimir_datos_de_configuracion()
			temp = temp.next

	def buscar_por_nombre(self, name):
		r_configuracion = None
		temp = self.first

		while temp != None:
			if temp.name == name:
				r_configuracion = temp
				break
			else:
				temp = temp.next

		return r_configuracion

	def buscar_por_posicion(self, pos):
		actual = self.first
		for i in range(pos-1):
			actual = actual.next
		return actual