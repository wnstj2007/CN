from multiprocessing import Process
import socket
import os

def send_recv(client):
    pass

def main(port):
    proc = None
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', port))
    serversocket.listen(5)
    client = []

    try:
        pass
    except Exception:
        proc.join()

if __name__ == '__main__':
    port = 8888
    main(port)