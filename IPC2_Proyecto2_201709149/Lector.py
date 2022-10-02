from tkinter import filedialog
from tkinter import *
from xml.dom import minidom

import Lista_empresas
import Lista_puntos
import Lista_escritorios
import Lista_transacciones
import Lista_clientes
import Lista_configuraciones

import Empresa
import Punto
import Escritorio
import Transaccion
import Cliente
import Configuracion

class Lector:

    file_root = None
    file = None    
    procesed_data = False

    list_of_processed_companies = None
    saved_settings = None

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

    def proces_file_1(self):
        if self.procesed_data == False:

            print("Procesando información de empresas...")
            print("")            
            lista_de_empresas = self.file.getElementsByTagName("empresa")        
            cant_empresas = len(lista_de_empresas)

            if cant_empresas != 0:

                for i in range(cant_empresas):
                    print("Obteniendo información de la empresa: #" + str(i+1) + "...")
                    print("     Verificando datos iniciales...")

                    id = ""
                    name = ""
                    abb = ""

                    try:
                        id = lista_de_empresas[i].attributes["id"].value
                        name = lista_de_empresas[i].getElementsByTagName("nombre")[0].childNodes[0].data
                        abb = lista_de_empresas[i].getElementsByTagName("abreviatura")[0].childNodes[0].data
                        print("     Empresa con nombre: " + name + ", abreviatura: " + abb + " e id: " + id)
                    except:                        
                        print("     No se han encontrado los atributos requerridos para el empresa. ")
                        print("     La empresa será omitida.")
                        continue
                   
                    company_points = lista_de_empresas[i].getElementsByTagName("listaPuntosAtencion")[0]
                    company_points = company_points.getElementsByTagName("puntoAtencion")
                    new_point_list = Lista_puntos.Lista_puntos()

                    for point_i in company_points:
                        point_id = point_i.attributes["id"].value
                        point_name = point_i.getElementsByTagName("nombre")[0].childNodes[0].data
                        point_address = point_i.getElementsByTagName("direccion")[0].childNodes[0].data
                        point_desk_list = point_i.getElementsByTagName("listaEscritorios")[0].getElementsByTagName("escritorio")
                        
                        new_desk_list = Lista_escritorios.Lista_escritorios()

                        for desk_i in point_desk_list:
                            desk_id = desk_i.attributes["id"].value
                            desk_ident = desk_i.getElementsByTagName("identificacion")[0].childNodes[0].data
                            desk_manager = desk_i.getElementsByTagName("encargado")[0].childNodes[0].data
                            new_desk = Escritorio.Escritorio(desk_id, desk_ident, desk_manager)
                            new_desk_list.add(new_desk)

                        new_point = Punto.Punto(point_id, point_name, point_address, new_desk_list)
                        new_point_list.add(new_point)

                    company_transactions = lista_de_empresas[i].getElementsByTagName("listaTransacciones")[0]
                    company_transactions = company_transactions.getElementsByTagName("transaccion")
                    new_transaction_list = Lista_transacciones.Lista_transacciones()

                    for transaction_i in company_transactions:
                        tr_id = transaction_i.attributes["id"].value
                        tr_name = transaction_i.getElementsByTagName("nombre")[0].childNodes[0].data
                        tr_a_time = transaction_i.getElementsByTagName("tiempoAtencion")[0].childNodes[0].data
                        new_transaction = Transaccion.Transaccion(tr_id, tr_name, tr_a_time, None)
                        new_transaction_list.add(new_transaction)

                    new_company = Empresa.Empresa(id, name, abb, new_point_list, new_transaction_list)
                    if self.list_of_processed_companies == None:
                        self.list_of_processed_companies = Lista_empresas.Lista_empresas()
                    self.list_of_processed_companies.add(new_company)

                print("")
                print("Información de empresas procesada correctamente.")
                print("")
            else:
                print("")
                print("No se han encontrado empresas.")
                print("")
        else:
            print("Ya se han procesado los datos para el actual archivo cargado en memoria.")
            print("")


    def proces_file_2(self):
        if self.procesed_data == False:

            print("Procesando información de configuraciones...")
            print("")            
            config_list = self.file.getElementsByTagName("listadoInicial")[0]
            config_list = config_list.getElementsByTagName("configInicial")
            cant_config = len(config_list)

            if cant_config != 0:

                for i in range(cant_config):
                    print("Obteniendo información de la configuración: #" + str(i+1) + "...")
                    print("     Verificando datos iniciales...")

                    config_id = ""
                    company_id = ""
                    point_id = ""                    

                    try:
                        config_id = config_list[i].attributes["id"].value
                        company_id = config_list[i].attributes["idEmpresa"].value
                        point_id = config_list[i].attributes["idPunto"].value
                    except:
                        print("     No se han encontrado los atributos requerridos para la configuración. ")
                        print("     La configuración será omitida.")
                        continue

                    desk_list = config_list[i].getElementsByTagName("escritoriosActivos")[0]
                    desk_list = desk_list.getElementsByTagName("escritorio")
                    new_desk_list = Lista_escritorios.Lista_escritorios()

                    for desk_i in desk_list:
                        desk_id = desk_i.attributes["idEscritorio"].value
                        new_desk = Escritorio.Escritorio(desk_id, None, None)
                        new_desk_list.add(new_desk)

                    client_list = config_list[i].getElementsByTagName("listadoClientes")[0]
                    client_list = client_list.getElementsByTagName("cliente")
                    new_client_list = Lista_clientes.Lista_clientes()

                    for client_i in client_list:
                        dpi = client_i.attributes["dpi"].value
                        client_name = client_i.getElementsByTagName("nombre")[0].childNodes[0].data
                        client_transactions = client_i.getElementsByTagName("listadoTransacciones")[0]
                        client_transactions = client_transactions.getElementsByTagName("transaccion")
                        new_transaction_list = Lista_transacciones.Lista_transacciones()

                        for tran_i in client_transactions:
                            tran_id = tran_i.attributes["idTransaccion"].value
                            tran_cant = tran_i.attributes["cantidad"].value
                            new_tran = Transaccion.Transaccion(tran_id, None, None, tran_cant)
                            new_transaction_list.add(new_tran)

                        new_client = Cliente.Cliente(dpi, client_name, new_transaction_list)
                        new_client_list.add(new_client)

                    new_config = Configuracion.Configuracion(config_id, company_id, point_id, new_desk_list, new_client)
                    if self.saved_settings == None:
                        self.saved_settings = Lista_configuraciones.Lista_configuraciones()
                    self.saved_settings.add(new_config)
                
                print("")                
                print("Información de configuraciones procesada correctamente.")
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
        self.list_of_processed_companies = None
        self.procesed_data = False
        self.piso_calculado = None