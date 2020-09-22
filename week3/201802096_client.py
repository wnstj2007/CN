import socket

IP = '10.0.2.15'
port = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, port))

message = 'hello server! I\'m client'
sock.send(message.encode())
data = sock.recv(1024)
sock.close()

print('received message : ' + data.decode())
