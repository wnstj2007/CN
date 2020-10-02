from threading import Thread
import socket
import os

def send_recv(client_socket):
    pass

def main(port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', port))
    th = None
    print('listening...')
    serversocket.listen(5)
    client = []

    try:
        pass
    except Exception:
        th.join()

if __name__ == '__main__':
    port = 8888
    main(port)