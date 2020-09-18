import socket

ip = ''
port = 5001

sock = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
sock.bind((ip, port))
sock.listen()

conn, addr = sock.accept()
print('Connection address : ' + str(addr))
