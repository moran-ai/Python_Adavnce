from socket import *

# 创建socket
server_socket = socket(AF_INET, SOCK_STREAM)

# 绑定ip
server_socket.bind(('', 8080))
# 让服务端处于被动
server_socket.listen(5)

while True:
    # 接收客户端发送的链接
    new_socket, client_host_port = server_socket.accept()
    print(client_host_port[0], client_host_port[1])

    while True:
        # 服务器接收数据
        data = new_socket.recv(1024)
        # print('客户端:', data.decode('utf-8'))

        if len(data) > 0:
            print(f'客户端{client_host_port[0]}:{client_host_port[1]}:', data.decode('utf-8'))
        if data.decode('utf-8') == 'exit':
            print(f'客户端{client_host_port[0]}:{client_host_port[1]}已经退出')
            break
        # 服务器发送数据
        send_data = input("send:")
        if len(send_data) > 0:
            new_socket.send(send_data.encode('utf-8'))
    new_socket.close()

server_socket.close()
