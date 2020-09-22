import socket
import random

ip = ''
port = 5001

sock = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
sock.bind((ip, port))
sock.listen()

clients = [{} for _ in range(3)]
for i in range(3):
	conn, addr = sock.accept()
	print('Connection address : ' + str(addr))
	clients[i]['conn'] = conn
	
for i in clients:
	i['conn'].send('Okay... All players have gathered. Start the game.'.encode())
while True:
	#난수 10개 생성
	numbers = [ random.randrange(1,101) for _ in range(10) ]
	for i in clients:
		#숫자 선택
		i['conn'].send('Please select 1 number from 1 to 10.')
		i['conn'].send('Number : '.encode())
		num = i['conn'].recv(1024)
		i['num1'] = numbers[num+1]
		i['num2'] = random.randrange(-1, 5)
		data = 'You chose the number ' + str(numbers[num+1]) + '. Please wait.'
		i['conn'].send(data.encode())
		
	for i in clients:
		#연산자 선택
		i['conn'].send('Do you want multiply or add...?'.encode())
		i['conn'].send('multiply or add : '.encode())
		oper = i['conn'].recv(1024).decode()
		if oper == 'add':
			i['score'] = i['num1']+i['num2']
		elif oper == 'multiply':
			i['score'] = i['num1']*i['num2']
		i['conn'].send('Okay... please wait.'.encode())
		
		
	for i in clients:
		pass
conn.close()
