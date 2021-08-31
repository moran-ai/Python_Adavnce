from socket import *

# 1. 建立UDP的socket
server_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 设定一个ip和端口
server_host_port = ('127.0.0.1', 8090)

# 3. 绑定一个IP和端口, 只有绑定了的socket才能称之为服务器端
server_socket.bind(server_host_port)
print('开始监听...')

while True:

    # 4. 打开监听-每次接收的最大为64k
    data = server_socket.recvfrom(1024)
    print(data)
    print(data[0].decode('utf-8'))

    # 4.1 回复相同的内容
    server_socket.sendto(data[0], data[1])

# 5. 关闭监听
s.close()
