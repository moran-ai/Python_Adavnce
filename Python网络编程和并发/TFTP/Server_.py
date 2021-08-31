import struct
from socket import *

# 创建socket  UDP协议
server_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定端口  TFTP默认端口为69
server_socket.bind(("", 69))


def download(filename, client_ip, client_port):
    # 创建一个新的socket来处理下载图片的请求
    new_socket = socket(AF_INET, SOCK_DGRAM)

    num = 1  # 块编号
    flag = True
    # 判断客户端请求的文件是否存在
    # 如果存在，打开这个文件
    try:
        f = open(filename, 'rb')
    # 不存在就发送一个错误信息给客户端
    except:
        msg = "该文件不存在"
        error_msg = struct.pack('!HH%dsb' % len(msg), 5, 5, msg.encode('utf-8'), 0)
        new_socket.sendto(error_msg, (client_ip, client_port))
        # exit()
        flag=False

    # 文件存在，开始读取
    while flag:
        data = f.read(512)
        # 将数据包发送给客户端
        # 进行数据包的压缩
        data_pakge = struct.pack('!HH', 3, num) + data
        # 数据包发送给客户端
        new_socket.sendto(data_pakge, (client_ip, client_port))

        # 判断客户端是否下载完成
        if len(data) < 512:
            print(f'客户端{client_ip}:{client_port}下载{filename}完成')
            break
        # 如果客户端没有下载完成，接收客户端发送过来的ACK确认码
        ack = new_socket.recvfrom(1024)
        # 获取操作码和块编号
        open_code, ack_num = struct.unpack('!HH', ack[0])
        print(f"客户端{client_ip}:{client_port}的确认码是:{ack_num}")
        num += 1
        if open_code != 4 or ack_num < 1:
            break
    new_socket.close()


# 服务器接收请求
def server():
    while True:
        client_data, (client_ip, client_port) = server_socket.recvfrom(1024)
        print(client_data, client_ip, client_port)

        # 判断请求是否正确
        if struct.unpack('!b5sb', client_data[-7:]) == (0, b'octet', 0):
            # 如果是获取操作码
            ope_code = struct.unpack('!H', client_data[0:2])
            print(f'客户端的操作码是:{ope_code}')
            # 获取文件名
            filename = client_data[2:-7].decode('utf-8')
            print(filename)
            # 判断是否是下载请求
            if ope_code[0] == 1:
                print(f'客户端{client_ip}:{client_port}想要下载--->{filename}')
                download(filename, client_ip, client_port)


if __name__ == '__main__':
    server()
