import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1000))
def handle_clients(clientsocket,adress,clients_array):
	while True:
		msg = clientsocket.recv(1000)
		msg = msg.decode("utf-8")
		for sending in range(len(clients_array)):
			clients_array[sending].send(bytes(msg,"utf-8"))

def start():
	s.listen(5)
	clients_array = []
	while True:
		clientsocket,adress = s.accept()
		clients_array.append(clientsocket)
		print(clients_array)
		clientsocket.send(bytes("welcome to the server!","utf-8"))
		th = threading.Thread(target=handle_clients,args=(clientsocket,adress,clients_array))
		th.start()
start()
