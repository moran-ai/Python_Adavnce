import struct
from socket import *

# 创建socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# 确定服务器的ip和端口
host_post = ('127.0.0.1', 69)

filename = input("请输入文件名：")

# 准备数据包
data_packge = struct.pack('!H%dsb5sb' % len(filename), 1, filename.encode('utf-8'), 0, 'octet'.encode('utf-8'), 0)

# 发送数据包给服务器
client_socket.sendto(data_packge, host_post)

# 创建一个空白文件，用来存储下载的文件  a:以附加方式打开只写文件，如果文件不存在，会自动创建
f = open('cl_' + filename, 'ab')

# 客户端接收服务器返回的数据包
while True:
    server_data, (server_ip, server_port) = client_socket.recvfrom(1024)
    # 对数据包进行解包
    # 获取数据包的操作码和块编号  共占4个字节
    open_code, ack_num = struct.unpack('!HH', server_data[0:4])
    if int(open_code) == 5:
        print('服务器：文件不存在')
        break

    # 如果不是错误的数据包，就保存内容
    f.write(server_data[4:])

    # 如果数据包的长度小于516，就代表下载成功
    if len(server_data) < 516:
        print("文件下载成功")
        break

    # 如果不小于，则客户端发送一个ACK确认到服务器
    ack_da = struct.pack('!HH', 4, ack_num)
    client_socket.sendto(ack_da, (server_ip, server_port))

f.close()
client_socket.close()