import time
import socket
from locust import User, task

class MyUser(User):
    @task
    def test(self):
        ip = '192.168.1.10'
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, 8888))
        data = 'GET / HTTP /1.1'
        client.send(data.encode)
        client.close()