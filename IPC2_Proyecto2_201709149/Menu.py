import Lector as LectorClass
import Escritor as WriterClass

import sys
from tkinter import filedialog
from tkinter import *
import re
import os

class Menu:

    reader_obj = LectorClass.Lector()
    escritor_obj = WriterClass.Escritor()

    def __init__(self, exit):
        self.exit = exit

    def imprimir_menu(self):
        print(" ╔═══════════════════════════════════════════════════════════════════════════╗")
        print(" ║                        M E N Ú   P R I N C I P A L                        ║")
        print(" ╚═══════════════════════════════════════════════════════════════════════════╝")
        print("")
        print("     [1] Configuración de empresas.")
        print("     [2] Realización de pruebas.")
        print("     [3] Manejo de puntos de atención.")
        print("     [4] Visualizar estructuras.")
        print("     [6] Salir.")
        print("")
        print(" Escriba el número de acuerdo a la opción que desee: ")

    def imprimir_menu_de_carga(self):
        print("")
        print(" ---------------- Carga de archivos: ----------------")
        print("")
        print(" [1] Escribir dirección")
        print(" [2] Seleccionar archivo")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")

    def print_submenu_1(self):
        print("")
        print(" ---------------- Configuración de empresas: ----------------")
        print("")
        print(" [1] Cargar archivo de configuración del sistema.")        
        print(" [2] Cargar archivo de configuración inicial.")
        print(" [3] Crear nueva empresa.")        
        print(" [4] Limpiar sistema.")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")
        print("")

        submenu_option_1 = 0
        try:
            submenu_option_1 = int(input())
        except:
            print("Opción no válida.")
            submenu_option_1 = 0

        if submenu_option_1 == 1:            
            print("Se cargará un archivo de entrada 1.")
            self.imprimir_menu_de_carga()
            selected_option_l = 0
            try:
                selected_option_l = int(input())
            except:
                print("Error de entrada. Intente de nuevo")
                print("")

            if selected_option_l == 1:
                if self.reader_obj.read_done:
                    print("Borrando datos anterioes...")
                    self.reader_obj.reset_all_r()
                    print("Escriba una ruta específica:")
                    root = input()
                    if root == "":
                        print("Dirección vacía.")
                        print("")
                    else:
                        self.reader_obj.file_root = root
                        if self.reader_obj.read_file():
                            print("Carga realizada exitosamente.")
                            print("")
                            self.reader_obj.read_done = True
                            self.reader_obj.proces_file_1()
            elif selected_option_l == 2:
                if self.reader_obj.read_done:
                    print("Borrando datos anterioes...")
                    self.reader_obj.reset_all_r()

                print("Elija el archivo para cargarlo:")

                if self.reader_obj.open_a_file():
                    if self.reader_obj.read_file():
                        print("Carga realizada exitosamente.")
                        print("")
                        self.reader_obj.read_done = True
                        self.reader_obj.proces_file_1()                                
                        back = True
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")                
        elif submenu_option_1 == 2: # CARGA DE ARCHIVO 2
            print("Se cargará un archivo de configuración inicial (entrada 2).")
            self.imprimir_menu_de_carga()
            selected_option_l = 0
            try:
                selected_option_l = int(input())
            except:
                print("Error de entrada. Intente de nuevo")
                print("")

            if selected_option_l == 1:
                if self.reader_obj.read_done:
                    print("Borrando datos anterioes...")
                    self.reader_obj.reset_all_r()
                    print("Escriba una ruta específica:")
                    root = input()
                    if root == "":
                        print("Dirección vacía.")
                        print("")
                    else:
                        self.reader_obj.file_root = root
                        if self.reader_obj.read_file():
                            print("Carga realizada exitosamente.")
                            print("")
                            self.reader_obj.read_done = True
                            self.reader_obj.proces_file_2()
            elif selected_option_l == 2:
                if self.reader_obj.read_done:
                    print("Borrando datos anterioes...")
                    self.reader_obj.reset_all_r()

                print("Elija el archivo para cargarlo:")

                if self.reader_obj.open_a_file():
                    if self.reader_obj.read_file():
                        print("Carga realizada exitosamente.")
                        print("")
                        self.reader_obj.read_done = True
                        self.reader_obj.proces_file_2()                                
                        back = True
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")  
        elif submenu_option_1 == 3:
            print("Se creará una empresa.")
        elif submenu_option_1 == 4:
            print("Se limpiará el sistema...")            
            self.reader_obj.reset_all_r()
            print("*** Sistema limpio.")

    def print_submenu_3(self):
        print("")
        print(" ---------------- Carga de archivos: ----------------")
        print("")
        print(" [1] Ver estado del punto de atención.")
        print(" [2] Activar escritorio de servicio.")
        print(" [3] Desactivar escritorio de servicio.")
        print(" [4] Atender cliente.")
        print(" [5] Solicitud de atención.")
        print(" [6] Simular actividad del punto de atención.")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")
 
    def mostrar_empresas_disponibles(self, modo):
        while True:
            n = 1
            temp = self.reader_obj.list_of_processed_companies.first

            print("")
            
            while temp != None:
                print(" [" + str(n) + "] " + temp.name)
                temp = temp.next
                n += 1

            print("")
            print("Escriba el número correspondiente al paciente que desee graficar su recorrido:")

            p_option = 0
            try:
                p_option = int(input())
            except:
                print("Opción no válida, ingrese un número.")
                continue

            total_patients = self.reader_obj.list_of_processed_companies.cant
            if p_option <= total_patients:
                p_selected = self.reader_obj.list_of_processed_companies.buscar_por_posicion(p_option)
                print("Se graficará al siguiente paciente:")
                p_selected.imprimir_datos_de_paciente()
                print("")
                self.escritor_obj.graficar_secuencia(p_selected)
            break

    def iniciar_menu(self):
        print("")
        while(self.exit == False):
            self.imprimir_menu()
            try:
                selected_option = int(input())
            except:
                print("Error de entrada. Intente de nuevo")
                print("")
                continue
            if selected_option == 1:
                self.print_submenu_1()
            elif selected_option == 2:
                print("")
                lista = self.reader_obj.list_of_processed_companies
                sin_empresas = False
                if lista != None:
                    if lista.first != None:
                        print("     ¯¨'*•~-.¸¸,.-~*'[ empresas cargados en memoria ]¯¨'*•~-.¸¸,.-~*'")
                        todos = self.mostrar_empresas_disponibles("b")
                    else:
                        sin_empresas = True
                else:
                    sin_empresas = True
                if sin_empresas:
                    print(" (!) No se encuentran empresas disponibles actualmente.")
                    print("")
            elif selected_option == 3:                
                if self.reader_obj.procesed_data:
                    print("     ¯¨'*•~-.¸¸,.-~*'[ empresas cargados en memoria ]¯¨'*•~-.¸¸,.-~*'")
                    self.reader_obj.list_of_processed_companies.mostrar_empresas()
                else:
                    print("")
                    print(" (!) No se encuentran empresas disponibles actualmente.")
                    print("")
            elif selected_option == 4:
                if self.reader_obj.procesed_data:
                    print("")
                    print(" Se realizará la escritura del archivo de salida en formato XML...")
                    lista = self.reader_obj.list_of_processed_companies
                    self.escritor_obj.write_out_XML(lista)
                else:
                    print("")
                    print(" (!) No se encuentran empresas disponibles actualmente.")
                    print("")
            elif selected_option == 5:
                print("")
                lista = self.reader_obj.list_of_processed_companies
                sin_empresas = False
                if lista != None:
                    if lista.first != None:
                        print("     ¯¨'*•~-.¸¸,.-~*'[ empresas cargados en memoria ]¯¨'*•~-.¸¸,.-~*'")
                        todos = self.mostrar_empresas_disponibles("a")
                    else:
                        sin_empresas = True
                else:
                    sin_empresas = True
                if sin_empresas:
                    print(" (!) No se encuentran empresas disponibles actualmente.")
                    print("")
            elif selected_option == 6:
                self.exit = True
                print("")
                print("Se cerrará el programa.")
                print(". . .")
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")