from socket import *

# 创建一个socket
client_socket = socket(AF_INET, SOCK_STREAM)

# 确定服务器的ip和端口
server_host_port = ('127.0.0.1', 8080)

# 客户端建立一个链接（不是用来进行数据传输）
client_socket.connect(server_host_port)

# 客户端发送数据
data = input("请输入:")
client_socket.send(data.encode('utf-8'))

# 客户端接收服务器返回数据
rec_data = client_socket.recv(1024)
print('客户端接收到的数据是:', rec_data.decode('utf-8'))

client_socket.close()