import time
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))
client_socket.send('hello'.encode('utf-8'))
time.sleep(5)
client_socket.send('hhaha'.encode('utf-8'))
client_socket.close()
