import Escritorio

class Lista_escritorios:

	first = None
	cant = 0

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