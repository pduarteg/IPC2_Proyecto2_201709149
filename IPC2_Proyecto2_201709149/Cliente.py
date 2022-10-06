import Lista_transacciones
import Transaccion

class Cliente:

	next = None
	to_select_transactions_list = None
	atention_time = 0 # Tiempo que tomará al cliente en atender sus propias transacciones.
	wait_med_time = 0 # Tiempo promedio que le tomará esperar al cliente.
	
	def __init__(self, dpi, name, transactions_list):
		self.dpi = dpi
		self.name = name
		self.transactions_list = transactions_list

	# Crea una copia de la lista de transacciones que puede ser eliminada sin perder
	# la información original para realizar más pruebas
	def create_to_select_transactions_list(self):
		list = Lista_transacciones.Lista_transacciones()
		temp = self.transactions_list.first

		while temp != None:
			new_T = Transaccion.Transaccion(temp.id, None, None, temp.cant)
			list.add(new_T)
			temp = temp.next
		self.to_select_transactions_list = list

	# Muestra las transacciones que aún no han sido elegidas
	def show_disp_transactions(self):
		if self.to_select_transactions_list != None:
			if self.to_select_transactions_list.first != None:
				n = 1
				temp = self.to_select_transactions_list.first
				print("")
				while temp != None:
					print(" [" + str(n) + "] " + temp.id)
					temp = temp.next
					n += 1
				print(" [0] Terminar selección.")
				print("")
				print(" Escriba el número de acuerdo a la transacción a seleccionar.")
			else:
				print(" (!) No quedan más transacciones para la prueba.")
		else:
			print(" (!) No hay transacciones disponibles para el cliente.")

	def round_values(self):
		self.atention_time = round(self.atention_time, 2)
		self.wait_med_time = round(self.wait_med_time, 2)
