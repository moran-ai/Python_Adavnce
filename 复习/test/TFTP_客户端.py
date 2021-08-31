# coding:utf-8
from socket import *
import struct  # 负责python数据结构和c语言数据结构的转换

file_name = input('请输入文件名：')

# 创建客户端的socket
s = socket(AF_INET, SOCK_DGRAM)

# 定义目标服务器的地址和端口号
host_port = ('127.0.0.1', 69)

# todo '!H%dsb5sb'代表格式
#  请求的数据包， 将python中的数据转换为c语言中的数据
#  ！：开头，
#  H：1，
#  %ds: 文件名filename.encode(encoding='utf-8')：文件名不止一个字符，到底有多少个字符需要在s前面加上%d，代表字符的个数，
#  %len(filename):表示文件名字的长度，文件名字的长度是多少，就传参给d为多少
#  b:0
#  5s:octet
#  b:0

# todo 把数据打成一个数据包，将filename和octet转换为字节类型
# struct：可以将python格式转换为c语言的格式
data_package = struct.pack('!H%dsb5sb' % len(file_name), 1, file_name.encode(encoding='utf-8'), 0,
                           'octet'.encode(encoding='utf-8'), 0)

# 把数据包发到目标服务器
s.sendto(data_package, host_port)

# 客户端首先要创建一个空白的文件
f = open('client_' + file_name, 'ab')

while True:
    # 客户端接收服务端发送的数据，数据中只有2种，1、下载文件内容数据报2、错误的数据报
    recv_data, (server_ip, server_port) = s.recvfrom(1024)
    operator_code, num = struct.unpack('!HH', recv_data[:4])  # 把前4个字节的数据解包出来
    if int(operator_code) == 5:  # 判断数据包是否是error信息报
        print('服务器返回：你要下载的文件不存在')
        break
    # 如果是文件内容的数据报，需要保存文件内容
    f.write(recv_data[4:])
    if len(recv_data) < 516:  # 意味着服务器传输过来的文件已经接收完了
        print('客户端下载成功')
        break

    # 客户端收到数据包之后，还需要发送一个确认ack数据包给服务端
    ack_package = struct.pack('!HH', 4, num)
    s.sendto(ack_package, (server_ip, server_port))

# 释放资源
f.close()
s.close()

