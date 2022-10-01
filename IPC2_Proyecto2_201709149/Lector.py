from tkinter import filedialog
from tkinter import *
from xml.dom import minidom

import Lista_empresas
import Lista_puntos
import Escritorio

class Lector:

    file_root = None
    file = None
    read_done = False
    procesed_data = False

    list_of_processed_companies = None

    def open_a_file(self):
        print("Se cargará un archivo...")
        open_correctly = True
        try:
            root = Tk()
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                filetypes=(("XML Input Files [IPC2]", "*.xml"), ("all files", "*.*")))            
            self.file_root = root.filename            
        except:
            print("Error de directorio")
            open_correctly = False

        if open_correctly == True:
            if self.file_root == "":
                print("Dirección vacía.")
                print("")

        return open_correctly
    
    def read_file(self):
        load_correctly = True
        print("")
        print("Se leerá el directorio...")
        try:
            self.file = minidom.parse(self.file_root)
        except:
            print("Archivo no encontrado o no válido.")
            print("")
            load_correctly = False

        return load_correctly

    def proces_file(self):
        if self.procesed_data == False:

            print("Procesando información de empresas...")
            print("")
            self.list_of_processed_companies = Lista_empresas.Lista_empresas()
            lista_de_empresas = self.file.getElementsByTagName("empresa")        
            cant_empresas = len(lista_de_empresas)

            if cant_empresas != 0:

                for i in range(cant_empresas):
                    print("Obteniendo información del paciente: #" + str(i+1) + "...")
                    print("     Verificando datos iniciales...")

                    try:
                        id = lista_de_empresas[i].attributes["id"].value
                        name = lista_de_empresas[i].getElementsByTagName("nombre")[0].childNodes[0].data
                        abb = lista_de_empresas[i].getElementsByTagName("abreviatura")[0].childNodes[0].data
                        print("     Empresa con nombre: " + name + ", abreviatura: " + abb + " y id: " + id)
                    except:                        
                        print("     No se han encontrado los atributos requerridos para el paciente. ")
                        print("     La empresa será omitida.")
                        continue
                   
                    company_points = lista_de_empresas[i].getElementsByTagName("listaPuntosAtencion")[0]
                    company_points = company_points.getElementsByTagName("puntoAtencion")

                    for point_i in company_points:
                        point_name = point_i.getElementsByTagName("nombre")[0].childNodes[0].data
                        point_address = point_i.getElementsByTagName("direccion")[0].childNodes[0].data
                        point_desk_list = point_i.getElementsByTagName("listaEscritorios")[0].getElementsByTagName("escritorio")
                        
                        for desk_i in point_desk_list:
                            desk_id = desk_i.attributes["id"].value
                            desk_ident = desk_i.getElementsByTagName("identificacion")[0].childNodes[0].data
                            desk_manager = desk_i.getElementsByTagName("encargado")[0].childNodes[0].data
                            new_desk = Escritorio.Escritorio(desk_id, desk_ident, desk_manager)

                    
                print("")
                self.procesed_data = True
                print("Información de empresas procesada correctamente.")
                print("")
            else:
                print("")
                print("No se han encontrado empresas.")
                print("")
        else:
            print("Ya se han procesado los datos para el actual archivo cargado en memoria.")
            print("")

    def reset_all_r(self):
        self.file_root = None
        self.file = None
        self.read_done = False
        self.list_of_processed_companies = None
        self.procesed_data = False
        self.piso_calculado = None