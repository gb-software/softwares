import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.56.1",1000))
msg = s.recv(1000)
input(msg.decode("utf-8"))
def command():
	c = input("adam-tech>")
	s.send(bytes(c,"utf-8"))
def answers(ports,host):
	msg = s.recv(1000)
	print("\nadam-tech>",msg.decode("utf-8"))
def start():
	ports = 1000
	host = "pro-hacker"
	while True:
		th = threading.Thread(target=answers,args=(ports,host))
		th.start()
		command()
start()