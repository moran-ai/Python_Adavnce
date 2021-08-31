import struct
from socket import *

# 创建socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 8080))
server_socket.listen(5)
new_socket, client_address = server_socket.accept()

# 创建一个空白文件，用来接收数据
f = open('服务端.mp3', 'wb')

# 接收客户端发送过来的数据
# 接收报头
header_data = new_socket.recv(4)
size = struct.unpack('!i', header_data)[0]

size_ = 0  # 用来标记接收的数据的大小
# 如果接收的数据大小小于实际大小，则进行循环接收
while size_ < size:
    # 接收1024的数据大小
    data = new_socket.recv(1024)
    # 标记需要加上接收到的数据长度
    size_ += len(data)
    f.write(data)

print('服务端接收完成')
f.close()
new_socket.close()
server_socket.close()
