import Lector as LectorClass
import re
import os

class Escritor:
	
	def writeDOT_G(self, name, matriz, periodo):
		print("Graficando la matriz: ")
		matriz.imprimir_matriz()
		sanas = matriz.contar_sanas()
		infectadas = matriz.filas*matriz.columnas - sanas
		print("")

		dirA = os.getcwd()
		dirB = dirA + "\\Grafica_periodo_n_[" + str(periodo) + "]"
			
		print("*** Creando gráfica en ruta específicada...")
		try:
			file = open(dirB, "w")
		except:
			print("La ruta específicada ha producido un error.")
			print("Ruta en conflicto: " + str(dirB))
			print("Creando gráfica en la ruta actual...")
			dirA = os.getcwd()
			dirB = dirA + "\\Grafica_periodo_n_[" + str(periodo) + "]"
			file = open(dirB, "w")

		print("*** Ruta de salida: " + str(dirB))

		# Inicia escritura
		file.write("graph paciente {\n")
		file.write("	layout=dot\n")
		# Etiqueta con información del periodo
		label = "Paciente: " + name + " periodo no: " + str(periodo)
		label += " sanas: " + str(sanas) + ", infectadas: " + str(infectadas)
		file.write("	label = \"" + label + "\"\n")
		file.write("	node [shape=box color=deeppink3 style=filled fillcolor=salmon]\n")
		file.write("\n")

		temp = None # temp es el nodo actual
		nodo_aux = matriz.raiz.abajo
		color = ""

		for j in range(matriz.filas):
			temp = nodo_aux.derecha
			for i in range(matriz.columnas):
				if temp.estado == False:
					color = "white"
				else:
					color = "black"
				file.write("	c" + str(temp.x) + str(temp.y) + "[label=\"\" fillcolor=" + color + "]\n")
				temp = temp.derecha
			nodo_aux = nodo_aux.abajo
		file.write("\n")
		
		for i in range(matriz.columnas + 1): #i:columnas
			row = ""
			if i == 0:
				continue
			for j in range(matriz.filas + 1): #j:filas
				if j == 0:
					continue
				if j == (matriz.filas - 1 + 1): #<- aquí filas
					row += "c" + str(i) + str(j)
				else:
					row += "c" + str(i) + str(j) + " -- "
			file.write("	" + row + "\n")

		file.write("\n")

		for i in range(matriz.filas + 1): #i:filas
			if i == 0:
				continue
			row = ""
			for j in range(matriz.columnas + 1): #j:columnas
				if j == 0:
					continue
				if j == (matriz.columnas - 1 + 1): #<- aquí columnas
					row += "c" + str(j) + str(i)
				else:
					row += "c" + str(j) + str(i) + " -- "
			file.write("	rank=same {" + row + "}\n")
		file.write("}")
		# Doc end

		print("*** Escritura terminada.")
		print("*** Gráfica creada correctamente. Se abrirá en breve...")
		file.close()
		#file = open(dirB)
		#dirC = str(dirB)
		#print("Se abrirá el archivo:")
		os.system("DOT -Tsvg -O Grafica_periodo_n_[" + str(periodo) + "]")
		#os.system("Grafica_periodo_n_[" + str(periodo) + "].svg")
		print("")

	def graficar_secuencia(self, paciente):
		paciente.diagnosticar(paciente.rejilla_inicial, True, True)
		lista = paciente.lista_recorrido
		t = lista.first
		p = 0

		print("Se imprimirán: " + str(lista.cant))
		while t != None:
			self.writeDOT_G(paciente.name, t, p)
			t = t.next
			p += 1

	def write_out_XML(self, lista):
		lista.diagnosticar_todos_los_pacientes()

		dirA = os.getcwd()
		dirB = dirA + "\\Diagnóstico_Salida.xml"
			
		print("*** Creando gráfica en ruta específicada...")
		try:
			file = open(dirB, "w")
		except:
			print("La ruta específicada ha producido un error.")
			print("Ruta en conflicto: " + str(dirB))
			print("Creando salida en la ruta actual...")
			dirA = os.getcwd()
			dirB = dirA + "\\Grafica"
			file = open(dirB, "w")

		print("*** Ruta de salida: " + str(dirB))

		# Inicia escritura
		file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
		file.write("<pacientes>\n")
		t = lista.first
		while t != None:

			file.write("	<paciente>\n")
			file.write("		<datospersonales>\n")
			file.write("			<nombre>" + t.name + "</nombre>\n")
			file.write("			<edad>" + str(t.age) + "</edad>\n")
			file.write("		</datospersonales>\n")
			file.write("		<periodos>" + str(t.period) + "</periodos>\n")
			file.write("		<m>" + str(t.m) + "</m>\n")
			file.write("		<resultado>" + str(t.caso_de_enfermedad) + "</resultado>\n")
			file.write("	</paciente>\n")
			t = t.next

		file.write("</pacientes>\n")
		# Fin de escritura de XML		
		file.close()
		print("*** Escritura de XML de salida terminada.")	
		print("")	