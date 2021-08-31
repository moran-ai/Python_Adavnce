from socket import *

# 创建一个UDP 协议的socket，然后发送一条数据到网络的另外一个进程


# 1. 创建一个套接字
client_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 定义一个接受信息的目标-元组（，）前面是服务器地址，后面是端口号
host_port = ('127.0.0.1', 8090)

flag = True

while flag:

    # 3. 准备要发送的数据，注意：准备的数据要经过encode处理为字节码，因为网络上传输数据的方式是字节传输，否则数据无法传输
    datas = input('请输入要传入的内容：').encode('utf-8')

    # 4. 发送数据
    client_socket.sendto(datas, host_port)
    print('发送完成')

    # 4.1 接收回馈信息
    data = client_socket.recv(2048)
    print('收到的信息', data.decode('utf-8'))

    # 4.1 设定退出通道
    if data.decode('utf-8') == 'exit':
        flag = False
        print('退出')

# 5. 关闭套接字连接,释放系统资源
client_socket.close()
