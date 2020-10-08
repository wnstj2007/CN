import select
import os
import socket

port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen()
  
input_list = [server]
while True:
	input_ready, write_ready, except_ready = select.select(input_list, [], [])
	for ir in input_ready:
		if ir == server:
			client, address = server.accept()
			input_list.append(client)
		else:
			data = ir.recv(1024)
			print("[client {}] {}".format(os.getpid(), data.decode()))
			data = "HTTP/1.1 200 OK\r\n"
			ir.send(data.encode())
			ir.close()
			input_list.remove(ir)
