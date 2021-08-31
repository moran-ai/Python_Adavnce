from socket import *

server_scoket = socket(AF_INET, SOCK_STREAM)
server_scoket.bind(('', 8080))
server_scoket.listen(5)
new_socket, client_address = server_scoket.accept()
print(f'{client_address[0]}:{client_address[1]}连接成功')
data = new_socket.recv(3)
print('data:', data)
data1 = new_socket.recv(10)  # 将第一个数据中没有接收完的数据继续进行接收
print('data1:', data1)
new_socket.close()
server_scoket.close()
