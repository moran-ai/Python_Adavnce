# coding:utf-8
from socket import *
import struct  # 负责python数据结构和c语言数据结构的转换

# 服务器端的socket      UDP协议
server_soc = socket(AF_INET, SOCK_DGRAM)

# 绑定IP和端口号（默认IP和端口号）     空字符串表示本机的所有地址
server_soc.bind(('', 69))


# 下载
def download(file_name, client_ip, client_port):
    # 创建一个新的socket，负责发送文件内容的数据包到客户端
    new_socket = socket(AF_INET, SOCK_DGRAM)
    # 文件内容数据包的计数器,其实就是块的编号
    num = 1
    # 定义服务客户端退出的标签
    flag = True

    try:
        f = open(file_name, 'rb')
    except:
        # 如果文件不存在，创建错误的数据包
        msg = '文件不存在'
        error_package = struct.pack('!HH%dsb' % len(msg), 5, 5, msg.encode('utf-8'),
                                    0)  # H 表示python的Integer转成c的没有符号的short，
        # 5s表示python中包含5个字符的字符串转成c语言的字符数组
        new_socket.sendto(error_package, (client_ip, client_port))  # 把错误数据包发送给客户端
        # 当前线程结束，socket结束当前客户端退出服务器
        flag = False
    # 如果文件存在，需要把文件的内容切成一个个的数据包发送给客户端，一个数据包位512个字节
    while flag:
        # 从文件内容中，读取512个字节
        read_data = f.read(512)
        print(len(read_data))
        # 创建一个数据报
        data_package = struct.pack('!HH', 3, num) + read_data
        # 发送数据包
        new_socket.sendto(data_package, (client_ip, client_port))
        if len(read_data) < 512:  # 文件内容的数据刚好读完
            print(f'客户端：{client_ip}，文件下载完成')
            break  # 当前客户端退出
        # 服务器接收ACK的确认数据
        recv_ack = new_socket.recvfrom(1024)  # 里面有数据包的内容，还有客户端的ip和端口
        operator_code, ack_num = struct.unpack('!HH', recv_ack[0])
        # print(ack_num)
        print(f'客户端{client_ip}的确认信息是{ack_num}')
        num += 1
        # 保护性代码
        if int(operator_code) != 4 or int(ack_num) < 1:  # 不正常的ack确认信息
            break
    new_socket.close()  # 客户端真正的退出了


# 服务器端的socket不用关闭

def server():
    while True:
        # todo 服务器等着客户端发送过来的数据，然后等着接收；服务端接收到的数据包括传输的数据，ip地址和端口号
        recv_data, (client_ip, client_port) = server_soc.recvfrom(1024)
        print(recv_data, client_ip, client_port)
        # todo 判断数据包是否是：客户端请求的数据包
        # 将字节数据后7位进行解包
        # 如果相等，则说明是读写请求操作
        if struct.unpack('!b5sb', recv_data[-7:]) == (0, b'octet', 0):
            # todo 得到操作码的值，才能知道是上传还是下载文件
            operator_code = struct.unpack('!H', recv_data[0:2])
            # todo 得到文件的名字，才知道要上传那个文件或者是下载那个文件
            file_name = recv_data[2:-7].decode('utf-8')
            print(file_name)
            # todo 如果等于1为下载的请求逻辑
            if operator_code[0] == 1:
                print(f'客户端想下载文件：{file_name}')
                download(file_name, client_ip, client_port)


if __name__ == '__main__':
    server()
