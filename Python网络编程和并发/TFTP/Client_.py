import struct
from socket import *

# 创建socket  UDP协议
client_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定端口  TFTP默认端口为69
host_port = ('127.0.0.1', 69)

filename = input("输入文件名：")

# 将文件名进行打包
data_packge = struct.pack('!H%dsb5sb' % len(filename), 1, filename.encode('utf-8'), 0, 'octet'.encode('utf-8'), 0)

# 将请求发送给服务器
client_socket.sendto(data_packge, host_port)

# 创建一个空白文件，用来存储文件
f = open('Client_' + filename, 'ab')

# 客户端接收服务器的请求
while True:
    server_data, (server_ip, server_port) = client_socket.recvfrom(1024)
    # print(server_data)
    # 获取操作码和块编号
    open_code, ack_num = struct.unpack('!HH', server_data[0:4])
    # print(open_code)
    if int(open_code) == 5:
        print('文件不存在')
        break

    f.write(server_data[4:])
    if len(server_data) < 516:
        print("下载完成")
        break

    # 没有下载完成，就向服务器发送ACK
    ack_page = struct.pack('!HH', 4, ack_num)
    client_socket.sendto(ack_page, (server_ip, server_port))
