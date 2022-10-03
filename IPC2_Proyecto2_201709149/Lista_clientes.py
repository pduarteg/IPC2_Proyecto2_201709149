import Cliente

class Lista_clientes:

	first = None
	cant = 0

	def add(self, cliente):
		if self.first == None:
			self.first = cliente
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = cliente
			self.cant += 1

	def mostrar_clientes(self):
		temp = self.first
		
		while temp != None:
			temp.imprimir_datos_de_cliente()
			temp = temp.next

	def buscar_por_nombre(self, name):
		r_cliente = None
		temp = self.first

		while temp != None:
			if temp.name == name:
				r_cliente = temp
				break
			else:
				temp = temp.next

		return r_cliente

	def buscar_por_posicion(self, pos):
		actual = self.first
		for i in range(pos-1):
			actual = actual.next
		return actual

	def take_next_client(self):
		client = self.first
		self.first = self.first.next
		self.cant -= 1
		return client