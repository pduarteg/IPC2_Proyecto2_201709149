import Lista_clientes
import Lista_transacciones
import Cliente
import Transaccion

class Simulator:

	# Variables de la simulación
    to_test_company = None
    to_test_point = None
    to_test_setting = None
    to_test_client_list = None # cola

    disp_client_list = None # Clientes que pueden usarse para la simulación
    test_initialized = False

    clients_in = 0 # Cantidad de clientes que han ingresado
    clients_done = 0 # Cantidad de clientes ya atendidos

    point_total_wait_time = 0
    point_min_wait_time = 0
    point_max_wait_time = 0
    point_med_time = 0
    point_min_a_time = 0
    point_max_a_time = 0

    actual_wait_time = 0 # Tiempo en minutos

    def reset_all(self): # PENDIENTES POR AGREGAR
        self.test_initialized = False   
        self.to_test_company = None
        self.to_test_point = None
        self.to_test_setting = None
        self.to_test_client_list = None

        self.clients_in = 0
        self.clients_done = 0

        self.point_total_wait_time = 0
        self.point_min_wait_time = 0
        self.point_max_wait_time = 0
        self.point_med_time = 0
        self.point_min_a_time = 0
        self.point_max_a_time = 0
        self.disp_client_list = None
        self.actual_wait_time = 0

    def finish_service(self):
        print(" *** Asignando clientes en cola a escritorios disponibles.")
        list = self.to_test_point.desk_list

        # Desasignando clientes
        temp = list.first
        while temp != None:
            temp.a_client = None
            temp = temp.next

        # Asignando clientes a escritorios
        temp = list.first
        while temp != None:
            if temp.state == True:
                if self.to_test_client_list.cant > 0:
                    client = self.to_test_client_list.take_next_client()
                    temp.a_client = client
                    print(" Asignando el cliente: " + client.name + ", al escritorio: " + temp.id)
                    print(" Atención en proceso...")
                    # Cálculo de tiempos:

                        # Tiempo medio de atención:
                    temp.total_clients_a += 1
                    temp.total_a_time += client.atention_time
                    temp.med_time = temp.total_a_time / temp.total_clients_a
                        # Tiempo mínimo de atención:
                    if temp.min_a_time == None:
                        temp.min_a_time = client.atention_time
                    elif client.atention_time < temp.min_a_time:
                        temp.min_a_time = client.atention_time
                        # Tiempo máximo de atención:
                    if temp.max_a_time == None:
                        temp.max_a_time = client.atention_time
                    elif client.atention_time > temp.max_a_time:
                        temp.max_a_time = client.atention_time
            temp = temp.next

    def initialize_test(self):
        # Crea la cola vacía
        self.to_test_client_list = Lista_clientes.Lista_clientes()        

        # Crea una copia de los posibles clientes
        print(" *** Cargando información de clientes...")
        self.disp_client_list = Lista_clientes.Lista_clientes()
        temp = self.to_test_setting.client_list.first
        while temp != None:
            new_client = Cliente.Cliente(temp.dpi, temp.name, temp.transactions_list)
            self.disp_client_list.add(new_client)
            temp = temp.next
        self.test_initialized = True

    def calculate_client_atention_time(self, client):
        a = 0
        t = client.transactions_list.first
        l = self.to_test_company.transaction_list
        while t != None:
            time = int(l.buscar_por_id(t.id).a_time)
            a += (time)*(int(t.cant))
            t = t.next
        client.atention_time = a
        print(" *** El cliente: " + client.name + ", tomará en atenderse: " + str(a) + " minutos.")

    def request_service(self):
        while True:
            print("")
            print(" *** Clientes disponibles para la prueba: ")
            print("")
            n = 1
            temp = self.disp_client_list.first
            while temp != None:
                print(" [" + str(n) + "] " + temp.name)
                temp = temp.next
                n += 1
            print("")
            print(" - Seleccione al cliente para agregar a la cola.")
            selected_client = 0

            try:
                selected_client = int(input())
            except:
                print(" (!) Selección no válida, intente de nuevo.")
                print("")
                continue

            if selected_client > 0 and selected_client <= self.disp_client_list.cant:
                print("")
                selected_client = self.disp_client_list.buscar_por_posicion(selected_client)
                if selected_client != None:
                    # Eligiendo transacciones
                    print("")
                    selected_client.create_to_select_transactions_list()
                    print(" Se ha seleccionado al cliente: " + selected_client.name)
                    new_transactions_list = Lista_transacciones.Lista_transacciones()
                    # Bucle de selección
                    while True:
                        print(" Transacciones restantes que puede realizar el cliente: ")
                        selected_client.show_disp_transactions()
                        if selected_client.to_select_transactions_list.cant > 0:
                            selected_transaction = None
                            entry = 0
                            try:
                                entry = int(input())
                            except:
                                print(" (!) Selección no válida, intente de nuevo.")
                                continue

                            if entry > 0 and entry <= selected_client.to_select_transactions_list.cant:
                                selected_transaction = selected_client.to_select_transactions_list.buscar_por_posicion(entry)
                                if selected_transaction != None:
                                    # Borrando transacción
                                    selected_client.to_select_transactions_list.delete_transaction(selected_transaction.id)
                                    # Creando transacción nueva
                                    new_transaction = Transaccion.Transaccion(selected_transaction.id, None, None, selected_transaction.cant)
                                    new_transactions_list.add(new_transaction)
                                    print(" *** Se ha agregado una transacción.")
                                    print("")
                                else:
                                    print(" *** No se ha podido agregar la transacción.")
                                    continue
                            elif entry == 0: # Dejar de elegir
                                if new_transactions_list.cant > 0:
                                    break
                                else:
                                    print(" (!) Debe seleccionar al menos una transacción.")
                                    continue
                    new_client = Cliente.Cliente(selected_client.dpi, selected_client.name, new_transactions_list)
                    self.to_test_client_list.add(new_client)
                    self.disp_client_list.delete_client(new_client.dpi)
                    print(" *** Se ha agregado al cliente: " + new_client.name +  " a la cola de atención.")

                    # Cálculo del tiempo
                    self.calculate_client_atention_time(new_client)                    
                    self.clients_in += 1
                    self.point_med_time = self.point_total_wait_time / self.clients_in
                    print(" *** El tiempo medio de espera para el cliente es: " + str(self.point_med_time) + " minutos.")
                    self.point_total_wait_time += new_client.atention_time
                    print("")
                    break                    
                else:
                    print(" (!) Ha ocurrido un error en la selección del cliente.")
            else:
                print(" (!) Selección no válida, intente de nuevo.")
                print("")