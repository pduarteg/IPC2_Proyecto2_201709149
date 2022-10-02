import Empresa

class Lista_empresas:

	first = None
	cant = 0

	def add(self, empresa):
		if self.first == None:
			self.first = empresa
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = empresa
			self.cant += 1

	def mostrar_empresas(self):
		temp = self.first
		
		while temp != None:
			temp.imprimir_datos_de_empresa()
			temp = temp.next

	def buscar_por_nombre(self, name):
		r_empresa = None
		temp = self.first

		while temp != None:
			if temp.name == name:
				r_empresa = temp
				break
			else:
				temp = temp.next

		return r_empresa

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