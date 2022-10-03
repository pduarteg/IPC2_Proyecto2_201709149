class Simulator:

	# Variables de la simulación
    to_test_company = None
    to_test_point = None
    to_test_setting = None
    to_test_client_list = None

    clients_done = 0 # Cantidad de clientes ya atendidos
    point_total_time = 0
    point_min_wait_time = 0
    point_max_wait_time = 0
    point_med_time = 0
    point_min_a_time = 0
    point_max_a_time = 0

    def reset_all(self):
    	self.to_test_company = None
    	self.to_test_point = None
    	self.to_test_setting = None
    	self.to_test_client_list = None
    	self.clients_done = 0
    	self.point_total_time = 0
    	self.point_min_wait_time = 0
    	self.point_max_wait_time = 0
    	self.point_med_time = 0
    	self.point_min_a_time = 0
    	self.point_max_a_time = 0