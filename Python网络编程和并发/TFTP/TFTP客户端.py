import struct  # 将python数据结构转为C数据结构
from socket import *

# 创建客户端的socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# 目标服务器的IP和端口 FTFP端口默认为69
host_port = ('127.0.0.1', 69)

# 发送数据包到服务器 数据包的格式:读写请求：操作码+文件名+0+模式+0
# 使用struct模块，将python数据结构转为C数据结构
file_name = input("请输入文件名：")
# octet是C的模式
# !H%dsb5sb代表格式：以!开头,H代表整型，s代表C里面的字符,b表示整型即0,5s代表5个字符即octet %ds文件名的长度
#  struct.pack打包
data_package = struct.pack('!H%dsb5sb' % len(file_name), 1, file_name.encode("utf-8"), 0, "octet".encode('utf-8'), 0)

# 客户端将数据包发送给服务端
client_socket.sendto(data_package, host_port)

# 客户端创建一个空白文件,用来存储下载的文件
f = open('client_' + file_name, 'ab')

while True:
    # 客户端接收服务端发送过来的数据包
    recv_data, (server_ip, server_port) = client_socket.recvfrom(1024)
    # 获取操作码和块编号 对数据包进行解包  数据包：操作码(2个字节) + 块编号(2个字节) + 数据(512)
    ope_code, ack_num = struct.unpack("!HH", recv_data[:4])
    # 判断返回的数据包是否是错误信息
    if int(ope_code) == 5:
        print("服务器:你要下载的文件不存在")
        break
    # 如果不是错误的数据包,就保存内容
    f.write(recv_data[4:])
    # 如果数据包的长度小于516,代表下载成功
    if len(recv_data) < 516:
        print("文件下载成功")
        break

    # 客户端在收到数据包,需要发送一个ACK确认信息给服务器
    # ACK：操作码(2个字节) + 块编号(2个字节)
    ack_packge = struct.pack("!HH", 4, ack_num)
    client_socket.sendto(ack_packge, (server_ip, server_port))

f.close()
client_socket.close()
