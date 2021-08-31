import struct
from socket import *

# 创建服务端的socket
socket_server = socket(AF_INET, SOCK_DGRAM)

# 绑定IP地址  69为默认端口
socket_server.bind(('', 69))


def download(filename, client_ip, client_port):
    """
    文件下载
    :param filename:  下载的文件名
    :param client_ip:  客户端的ip地址
    :param client_port: 客户端的端口  会打开一个新的端口
    :return:
    """
    # 创建一个新的socket，用来处理客户端下载请求
    new_socket = socket(AF_INET, SOCK_DGRAM)

    # 文件内容的数据包有多个，创建一个数据包的计数器  块编号
    num = 1
    flag = True
    try:
        f = open(filename, 'rb')
    except:
        # 错误数据包格式：ERROR:操作码(2个字节) + 差错码(2个字节) + 差错信息(n个字节) + 0(1个字节)
        msg = "该文件不存在"
        # 错误数据包 !HH%dsb 表示格式 H将pyhon中的数字转为C中的可变的数 s将python中的字符转为C中的字符数组
        error_packge = struct.pack('!HH%dsb' % len(msg), 5, 5, msg.encode('utf-8'), 0)
        # 将错误数据包发给客户端
        new_socket.sendto(error_packge, (client_ip, client_port))
        # 当前线程退出客户端
        flag = False

    # 如果请求的文件存在 需要将文件的内容切成一个个的数据包发送给客户端 一个数据包的大小为512字节
    while flag:
        read_data = f.read(512)
        # 创建数据包
        data_packge = struct.pack("!HH", 3, num) + read_data
        # 发送文件内容数据包给客户端
        new_socket.sendto(data_packge, (client_ip, client_port))
        if len(read_data) < 512:  # 代表已经下载完成
            print(f'客户端: {client_ip}:{client_port} ---> {filename}下载完成')
            # exit()  # 下载完成后退出
            # flag = False
            break
        # 没有下载完成,服务端继续接收客户端的请求
        # 接收ACK确认  ACK：操作码(2个字节) + 块编号(2个字节)
        recv_ack = new_socket.recvfrom(1024)
        # 将接收到的客户端ACK请求进行解包
        ope_code, ack_num = struct.unpack("!HH", recv_ack[0])
        print(f"客户端: {client_ip}:{client_port}的确认信息是{ack_num}")
        num += 1
        # 如果客户端的操作码不等于4或者ACK确认信息小于1
        if int(ope_code) != 4 or int(ack_num) < 1:  # 不正确的ack确认信息
            # exit()
            # flag = False
            break
    # if f:
    #     f.close()
    # 退出socket
    new_socket.close()


# 循环接收客户端的信息
def server():
    while True:
        # 服务器等待客户端发送消息
        data, (ip_, port_) = socket_server.recvfrom(1024)
        # 打印接收到的信息
        print(data, ip_, port_)

        # 对收到的数据进行解包 data[-7:] 取最后7个字节
        # 读写请求：操作码(2个字节) + 文件名(n个字节) + 0(1个字节) + 模式(n个字节) + 0(1个字节)
        # struct.unpack 解包
        if struct.unpack('!b5sb', data[-7:]) == (0, b'octet', 0):
            # 获取操作码  操作码占2个字节 [0:2] 从索引0取到索引为1的位置
            ope_code = struct.unpack("!H", data[0:2])

            # 获取文件名
            filename = data[2:-7].decode('utf-8')
            print(ope_code, filename)

            if ope_code[0] == 1:
                print(ip_, ":", port_, "想要下载", filename)
                download(filename, ip_, port_)


if __name__ == '__main__':
    server()
