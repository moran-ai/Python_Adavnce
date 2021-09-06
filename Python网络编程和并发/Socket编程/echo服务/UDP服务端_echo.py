from socket import *

# 创建一个服务端的socket
socet_server = socket(AF_INET, SOCK_DGRAM)

# 创建服务端的IP地址和端口号  如果服务器有多个网卡，就会有多个IP，绑定IP地址使用''
host_post = ("", 8080)

# Socket绑定这个IP地址和端口号 只有绑定了端口号和地址 才能成为服务端的Socket
socet_server.bind(host_post)

# 服务器不断接收客户端发送的消息
while True:
    # 接收客户端发送过来的数据  接收1KB的数据  1KB=1024
    # 收到的数据是一个元组，第一个值是收到的内容 第二个值是IP地址 第三个值是端口号
    data = socet_server.recvfrom(1024)
    # print(data)
    # 需要对接收到的数据进行解码
    data_ = data[0].decode("utf-8")
    print(data[1], "发送的消息是：", data_)

    # 将收到的信息返回给客户端
    socet_server.sendto(data[0], data[1])

# 关闭套接字  释放资源
socet_server.close()
