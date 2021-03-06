import socket
import random

ip = '192.168.1.10'
port = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen()

clients = [{} for _ in range(3)]
for i in range(3):
	conn, addr = sock.accept()
	print('Connection address : ' + str(addr))
	clients[i]['conn'] = conn
	
for i in clients:
	i['conn'].send('Okay... All players have gathered. Start the game.'.encode())

#난수 10개 생성
numbers = [ random.randrange(1,101) for _ in range(10) ]
scores = []
for i in clients:
	#숫자 선택
	i['conn'].send('Please select 1 number from 1 to 10.'.encode())
	num = int(i['conn'].recv(1024).decode())
	i['num1'] = numbers[num-1]
	i['num2'] = random.randrange(-1, 5)
	data = 'You chose the number ' + str(numbers[num-1]) + '. Please wait.'
	i['conn'].send(data.encode())
	
for i in clients:
	#연산자 선택
	i['conn'].send('Do you want multiply or add...?'.encode())
	oper = i['conn'].recv(1024).decode()
	#점수 계산
	if oper == 'add':
		i['score'] = i['num1']+i['num2']
	elif oper == 'multiply':
		i['score'] = i['num1']*i['num2']
	scores.append(i['score'])
	i['conn'].send('Okay... please wait.'.encode())
scores.sort()

for i in clients:
	#가장 높은 점수를 가진 client에게 승리 메시지를 보낸다.
	if i['score'] == scores[2]:
		i['conn'].send('Congratuations. You won!'.encode())
	else:
		i['conn'].send('Unfortunately, you hav been defeated.'.encode())
conn.close()
