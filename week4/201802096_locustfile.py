import time
import socket
from locust import User, task, between

class MyUser(User):
    @task
    def test(self):
        wait_time = between(1, 2)

        ip = '192.168.1.10'
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, 8888))
        data = 'GET / HTTP /1.1'
        client.send(data.encode)
        data = client.recv(1024)
        client.close()