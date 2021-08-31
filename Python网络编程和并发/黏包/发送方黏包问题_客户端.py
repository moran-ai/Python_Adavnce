from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8088))
client_socket.send('hello'.encode('utf-8'))
client_socket.send('word'.encode('utf-8'))
client_socket.close()