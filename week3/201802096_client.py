import socket

IP = '192.168.1.10'
port = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, port))


print(sock.recv(50).decode())

#숫자 입력
print(sock.recv(1024).decode())
num = int(input('Number : '))
sock.send(str(num).encode())
print(sock.recv(1024).decode())

#연산자 입력
print(sock.recv(1024).decode())
oper = input('multiply or add : ')
sock.send(oper.encode())
print(sock.recv(20).decode())

#결과
print(sock.recv(1024).decode())
	
sock.close()
