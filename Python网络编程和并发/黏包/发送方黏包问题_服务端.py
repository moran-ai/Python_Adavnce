from socket import *

# 创建socket
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', 8088))

server_socket.listen(5)

new_socket, client_address = server_socket.accept()
data = new_socket.recv(1024)
data1 = new_socket.recv(1024)
print('第一条数据：',data)
print('第二条数据：',data1)