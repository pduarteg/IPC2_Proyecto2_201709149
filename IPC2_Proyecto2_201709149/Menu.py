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

    # Variables de la simulación
    to_test_company = None
    to_test_point = None

    def __init__(self, exit):
        self.exit = exit

    def imprimir_menu(self):
        print(" ╔═══════════════════════════════════════════════════════════════════════════╗")
        print(" ║                        M E N Ú   P R I N C I P A L                        ║")
        print(" ╚═══════════════════════════════════════════════════════════════════════════╝")
        print("")
        print("     [1] Configuración de empresas.")
        print("     [2] Selección de empresa y punto de atención.")
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
        print(" [5] Volver al menú principal.")
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
        elif submenu_option_1 == 3: # Creación de empresa (manual)
            print("Se creará una empresa.")
        elif submenu_option_1 == 4: # Limpieza de las estructuras
            print("Se limpiará el sistema...")            
            self.reader_obj.reset_all_r()
            print("*** Sistema limpio.")
        elif submenu_option_1 == 5: # Volver a menú principal.
            print(" Volviendo al menú principal...")
            print("")
 
    def mostrar_empresas_disponibles(self):        
        while True:
            n = 1
            temp = self.reader_obj.list_of_processed_companies.first
            
            while temp != None:
                print(" [" + str(n) + "] " + temp.name)
                temp = temp.next
                n += 1
            print(" [0] Volver sin seleccionar")

            print("")
            print("Escriba el número correspondiente a la empresa para realizar la prueba:")

            p_option = 0
            try:
                p_option = int(input())
            except:
                print("Opción no válida, ingrese un número.")
                continue

            total_companies = self.reader_obj.list_of_processed_companies.cant
            if p_option <= total_companies and p_option != 0:
                p_selected = self.reader_obj.list_of_processed_companies.buscar_por_posicion(p_option)
                print("Se ha seleccionado a la empresa:")
                p_selected.imprimir_datos_de_empresa()

                self.to_test_company = p_selected
                print("")
                self.mostrar_puntos_disponibles(p_selected)
                print("")
            elif p_option == 0:
                print(" Volviendo al menú principal...")
                break
            break

    def mostrar_puntos_disponibles(self, company):
        while True:
            n = 1
            temp = company.point_list.first
            
            while temp != None:
                print(" [" + str(n) + "] " + temp.name)
                temp = temp.next
                n += 1

            print("")
            print("Escriba el número correspondiente al punto para realizar la prueba:")

            p_option = 0
            try:
                p_option = int(input())
            except:
                print(" (!) Opción no válida, ingrese un número.")
                continue

            total_points = company.point_list.cant
            if p_option <= total_points:
                p_selected = company.point_list.buscar_por_posicion(p_option)
                print(" *** Se ha seleccionado al punto:")
                p_selected.imprimir_datos_de_punto()

                self.to_test_point = p_selected
                print("")
                print(" *** Preparación para prueba completada.")
                print("")
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
            elif selected_option == 2: # Selección de empresa y punto de atención
                print("")
                print("     ¯¨'*•~-.¸¸,.-~*'[ Selección de Empresa y Punto de Atención ]¯¨'*•~-.¸¸,.-~*'")
                print("")
                if self.reader_obj.list_of_processed_companies != None:
                    self.mostrar_empresas_disponibles()
                else:
                    print(" (!) No se han cargado empresas.")
                    print("")

            elif selected_option == 3:
                print("")
                print("     ¯¨'*•~-.¸¸,.-~*'[ Manejo de Puntos de Atención ]¯¨'*•~-.¸¸,.-~*'")
                print("")
                print(" [1] Ver estado del punto de atención.")
                print(" [2] Activar escritorio de servicio.")
                print(" [3] Desactivar escritorio.")
                print(" [4] Atender cliente.")
                print(" [5] Solicitud de atención.")
                print(" [6] Simular actividad del punto de atención.")
                print("")
                print(" Escriba el número de acuerdo a la opción que desee: ")

                submenu_selected_option_3 = 0

                try:
                    submenu_selected_option_3 = int(input())
                except:
                    print(" *** Error de entrada, debe ingresar un número.")
                    submenu_selected_option_3 = 0

                if submenu_selected_option_3 == 1:
                    print("submenu 3 opción 1")
                    if self.to_test_company != None and self.to_test_point != None:
                        print("[PENDIENTE] ESTADO DEL PUNTO Y EMPRESA")
                    else:
                        print(" *** No se ha seleccionado una empresa y punto de atención para realizar las pruebas.")
                        print("")

                elif submenu_selected_option_3 == 2:
                    print("submenu 3 opción 2")
                elif submenu_selected_option_3 == 3:
                    print("submenu 3 opción 3")
                elif submenu_selected_option_3 == 4:
                    print("submenu 3 opción 4")
                elif submenu_selected_option_3 == 5:
                    print("submenu 3 opción 5")
                elif submenu_selected_option_3 == 6:
                    print("submenu 3 opción 6")

            elif selected_option == 4:
                print("menu 4")
            elif selected_option == 5:
                print("menu 5")
            elif selected_option == 6:
                self.exit = True
                print("")
                print("Se cerrará el programa.")
                print(". . .")
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")