import Transaccion

class Lista_transacciones:

	first = None
	cant = 0

	def add(self, transaccion):
		if self.first == None:
			self.first = transaccion
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = transaccion
			self.cant += 1

	def mostrar_transaccions(self):
		temp = self.first
		
		while temp != None:
			temp.imprimir_datos_de_transaccion()
			temp = temp.next

	def buscar_por_nombre(self, name):
		r_transaccion = None
		temp = self.first

		while temp != None:
			if temp.name == name:
				r_transaccion = temp
				break
			else:
				temp = temp.next

		return r_transaccion

	def buscar_por_posicion(self, pos):
		actual = self.first
		for i in range(pos-1):
			actual = actual.next
		return actual