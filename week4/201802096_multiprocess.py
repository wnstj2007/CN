from multiprocessing import Process
import socket
import os

def send_recv(client):
	data = client.recv(1024)
	print("[client {}] {}".format(os.getpid(), data.decode()))
	data = "HTTP/1.1 200 OK\r\n"
	client.send(data.encode())
	client.close()

def main(port):
	proc = None
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('', port))
	serversocket.listen(5)
	client = []

	try:
		while True:
			cli, address = serversocket.accept()
			print("accept client from", address)
			proc = Process(target = send_recv, args = (cli,))
			proc.start()
	except Exception:
		proc.join()

if __name__ == '__main__':
	port = 8888
	main(port)
