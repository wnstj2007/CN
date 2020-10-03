import socket
import os
import time

def send_recv(client_socket):
    data = client_socket.recv(1024)
    print('client {}] {}'.format(os.getpid(), data.decode()))
    response = 'HTTP/1.1 200 OK\r\n'
    client_socket.send(response.encode('utf-8'))
    client_socket.send(data)
    client_socket.close()

def main(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen()

    while True:
        (client, address) = server.accept()
        send_recv(client)

if __name__ == '__main__':
    port = 8888
    main(port)