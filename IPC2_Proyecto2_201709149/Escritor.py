import Lector as LectorClass
import re
import os

class Escritor:
	
	# tipo == 1: solo activos, == 2: solo inactivos, == 3: ambos.
	def writeDOT(self, a_point, a_line, tipo):
		print("Graficando el estado del punto de atención: ")
		dirA = os.getcwd()
		dirB = dirA + "\Estado"
			
		print("*** Creando gráfica en ruta específicada...")
		try:
			file = open(dirB, "w")
		except:
			print("La ruta específicada ha producido un error.")
			print("Ruta en conflicto: " + str(dirB))
			print("Creando gráfica en la ruta actual...")
			dirA = os.getcwd()
			dirB = dirA + "\Estado"
			file = open(dirB, "w")

		print("*** Ruta de salida: " + str(dirB))

		# Inicia escritura
		file.write("digraph Estado {\n")
		file.write("	layout=dot\n")

		# Etiqueta con información del punto de atención
		label = "Estado del punto y escritorios activos del punto."
		file.write("	rankdir=\"LR\"\n")
		file.write("	label = \"" + label + "\"\n")
		file.write("	node [shape=box color=deeppink3 style=filled fillcolor=salmon]\n")
		file.write("\n")

		# Datos del punto
		a_point.round_values()
		a_point.desk_list.contar_todos()

		R1_label = ""
		R1_label += a_point.name + "\\n"
		if a_point.med_wait_time > 0:
			R1_label += "Promedio espera: " + str(a_point.med_wait_time) + " min\\n"
		if a_point.max_wait_time > 0:
			R1_label += "Máximo espera: " + str(a_point.max_wait_time) + " min\\n"
		if a_point.min_wait_time > 0:
			R1_label += "Mínimo espera: " + str(a_point.min_wait_time) + " min\\n"
		if a_point.med_a_time > 0:
			R1_label += "Promedio atención: " + str(a_point.med_a_time) + " min\\n"
		if a_point.max_a_time > 0:
			R1_label += "Máximo atención: " + str(a_point.max_a_time) + " min\\n"
		if a_point.min_a_time > 0:
			R1_label += "Mínimo atención: " + str(a_point.min_a_time) + " min\\n"
		
		R1_label += "Escritorios activos: " + str(a_point.desk_list.active_n) + "\\n"
		R1_label += "Escritorios inactivos: " + str(a_point.desk_list.unactive_n)
		file.write("	R1 [label=\"Punto de atencion: " + R1_label + "\" shape=\"Mrecord\"]\n")

		file.write("	R2 [label=\"Clientes en espera:\" shape=\"Mrecord\"]\n")

		# Escritura de escritorios
		t = a_point.desk_list.first
		n = 0
		label = ""
		while t != None:
			if t.state and tipo == 1: # Mostrar activos
				t.round_values()
				label += "Escritorio: " + t.id + "\\n"
				label += "Identificación: " + t.identification + "\\n"
				label += "Encargado: " + t.manager + "\\n"
				if t.min_a_time != None:
					if t.min_a_time > 0:
						label += "Mínimo atención: " + str(t.min_a_time) + " min\\n"
				if t.max_a_time != None:
					if t.max_a_time > 0:
						label += "Máximo atención: " + str(t.max_a_time) + " min\\n"
				if t.med_time > 0:
					label += "Promedio atención: " + str(t.med_time) + " min\\n"
				label += "Atendidos: " + str(t.total_clients_a)
				file.write("	D" + str(n) + " [label=\"" + label + "\"]\n")
				n += 1
			elif t.state == False and tipo == 2: # Mostrar inactivos
				label += "Escritorio: " + t.id + "\\n"
				label += "Identificación: " + t.identification + "\\n"
				label += "Encargado: " + t.manager + "\\n"
				label += "Tiempo de atención medio: " + str(t.med_time)
				file.write("	D" + str(n) + " [label=\"" + label + "\"]\n")
				n += 1
			elif tipo == 3:
				label += "Escritorio: " + t.id + "\\n"
				label += "Identificación: " + t.identification + "\\n"
				label += "Encargado: " + t.manager + "\\n"
				label += "Tiempo de atención medio: " + str(t.med_time)
				file.write("	D" + str(n) + " [label=\"" + label + "\"]\n")
				n += 1
			label = ""
			t = t.next

		# Escritura de clientes
		t = a_line.first
		if t == None:
			label = "Sin clientes en la cola actual"
			file.write("	C0 [label=\"" + label + "\"]\n")
		else:
			n = 0
			label = ""
			while t != None:
				t.round_values()
				label += t.name + "\\n"
				label += "DPI: " + t.dpi + "\\n"
				label += "Atención propia: " + str(t.atention_time) + " min\\n"
				label += "Espera media: " + str(t.wait_med_time) + " min"
				file.write("	C" + str(n) + " [label=\"" + label + "\"]\n")
				label = ""
				n += 1
				t = t.next
		file.write("\n")

		# Unión de los nodos escritorios
		file.write("	{\n")		
		if tipo == 1:
			m = a_point.desk_list.active_n
			for i in range(m):
				file.write("		R1->D" + str(i) + "\n")				

		m = a_line.cant
		if m > 0:
			for i in range(m):
				if i == 0:
					file.write("		R2->C0\n")
				else:
					file.write("		C"  + str(i-1) + "->C" + str(i) + "\n")
		elif m == 0:
			file.write("		R2->C0\n")
		file.write("	}\n")
		file.write("}")
		# Doc end

		print("*** Escritura terminada.")
		print("*** Gráfica creada correctamente. Se abrirá en breve...")
		file.close()
		#file = open(dirB)
		#dirC = str(dirB)
		print("Se abrirá el archivo:")
		os.system("DOT -Tsvg -O Estado")
		os.system("Estado.svg")
		print("")