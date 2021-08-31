from socket import *

"""
客户端可以发送多条信息
客户端如果发送一个exit则退出
服务端如果获取到了什么就响应什么
"""

# 定义一个标志位，用来判断
flag = True

while flag:

    # 创建一个UDP协议的套接字 发送数据到网络上的另外一个进程
    client_sock = socket(AF_INET, SOCK_DGRAM)

    # 定义一个接收消息的目标  127.0.0.1 为服务器的ip地址  8080为端口号
    server_host_port = ('127.0.0.1', 8080)

    # 准备发送的数据  需要将输入的内容进行编码 编码为字节bytes
    data = input("请输入：").encode('utf-8')

    # 发送数据  在网络中使用ip+端口+协议标识一个进程
    client_sock.sendto(data, server_host_port)

    # 接收服务器返回的数据  并进行解码
    data_ = client_sock.recvfrom(1024)[0].decode('utf-8')
    print("服务器返回的数据是:", data_)

    # 对输入的数据进行解码，如果等于exit，退出客户端
    if data.decode('utf-8') == "exit":
        flag = False

# 关闭套接字  释放系统资源
client_sock.close()
