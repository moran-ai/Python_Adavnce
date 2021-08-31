import struct
from socket import *

# 创建socket  基于UDP协议
server_sokcet = socket(AF_INET, SOCK_DGRAM)

# 绑定端口和ip  ''代表本机所有的ip
server_sokcet.bind(('', 69))


def download(filename, client_ip, client_port):
    # 创建一个新的socket, 用来处理文件下载
    new_socket = socket(AF_INET, SOCK_DGRAM)

    # 判断客户端发送过来的数据  是否是正确的
    # 将内容划分为一个个的数据包，一个数据包有512字节大小
    num = 1  # 数据包的计数器
    flag = True
    # 如果客户端请求的文件存在，就进行打开
    try:
        # r打开可读文件，该文件必须存在
        f = open(filename, 'rb')
    #  客户端请求的文件不存在，就返回一个错误的数据包
    except:
        msg = '文件不存在'
        error_packge = struct.pack('!HH%dsb' % len(msg), 5, 5, msg.encode('utf-8'), 0)
        new_socket.sendto(error_packge, (client_ip, client_port))
        # exit()  # 退出客户端
        flag = False

    # 客户端请求的文件存在,将内容切分成一个个的数据包 大小为512
    while flag:
        # 读取数据
        read_data = f.read(512)
        # 创建数据包
        data_packge = struct.pack('!HH', 3, num) + read_data
        # 将数据包发送给客户端
        new_socket.sendto(data_packge, (client_ip, client_port))

        # 判断内容是否下载完毕
        if len(read_data) < 512:
            print(f'客户端{client_ip}:{client_port}---->{filename}下载完成')
            break

        # 如果没有下载完成，服务器需要接收客户端发送的ACK确认
        ack_data = new_socket.recvfrom(1024)

        # 对这个ACK确认进行一个解包
        open_code, ack_num = struct.unpack('!HH', ack_data[0])
        print(f'客户端{client_ip}:{client_port}确认的ACK是{ack_num}')
        num += 1  # 块编号加1
        # 对操作码和ACK进行判断  初始的ACK为1
        # 如果操作码不等于4或者ACK的长度小于1，则代表是错误的ACK和操作码
        if int(open_code) != 4 or ack_num < 1:
            break

    # 关闭新的socket
    new_socket.close()


def server():
    while True:
        # 服务器等待客户端发送请求 读写请求
        client_data, (client_ip, client_port) = server_sokcet.recvfrom(1024)
        print(client_data, client_ip, client_port)

        # 解包
        if struct.unpack('!b5sb', client_data[-7:]) == (0, b'octet', 0):
            # 获取操作码  2个字节
            open_code = struct.unpack('!H', client_data[0:2])
            # 获取文件名
            filename = client_data[2:-7].decode('utf-8')
            print(open_code, filename)

            # 根据操作码，决定客户端需要做什么
            if open_code[0] == 1:
                print(f"客户端{client_ip}:{client_port}需要下载{filename}")
                download(filename, client_ip, client_port)


if __name__ == '__main__':
    server()
