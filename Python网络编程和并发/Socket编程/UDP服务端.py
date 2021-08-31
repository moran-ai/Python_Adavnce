from socket import *

# 创建一个socket  遵循UDP协议
socket_server = socket(AF_INET, SOCK_DGRAM)

# 创建服务端的socket  ip+端口
host_port = ("127.0.0.1", 8080)

# 绑定端口
socket_server.bind(host_port)

# 接收客户端发送的消息  大小为1KB
data = socket_server.recvfrom(1024)

# 对数据进行解码
print(data[0].decode('utf-8'))

# 关闭socket
socket_server.close()