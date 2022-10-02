import Punto

class Lista_puntos:

	first = None
	cant = 0

	def add(self, punto):
		if self.first == None:
			self.first = punto
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = punto
			self.cant += 1

	def mostrar_puntos(self):
		temp = self.first
		
		while temp != None:
			temp.imprimir_datos_de_punto()
			temp = temp.next

	def buscar_por_nombre(self, name):
		r_punto = None
		temp = self.first

		while temp != None:
			if temp.name == name:
				r_punto = temp
				break
			else:
				temp = temp.next

		return r_punto

	def buscar_por_posicion(self, pos):
		actual = self.first
		for i in range(pos-1):
			actual = actual.next
		return actual

	def buscar_por_id(self, id):
		temp = self.first

		while temp != None:
			if temp.id == id:
				break
			temp = temp.next
		return temp