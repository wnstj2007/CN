import select
import os
import socket

port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen()
  
input_list = [server]
while True:
	for ir in input_ready:
		if ir == server:
			client, address = server.accept()
			print(address, 'is connected', flush=True)
			input_list.append(client)
        else:
			data = ir.recv(size)
			if data:
				print(ir.getpeername(), 'send :', data, flush=True)
				ir.send(data)
			else:
				print(ir.getpeername(), 'close', flush=True)
				ir.close()
				input_list.remove(ir)
