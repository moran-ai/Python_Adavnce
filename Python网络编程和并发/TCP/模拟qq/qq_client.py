from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

while True:
    data_ = input("send:")
    # 客户端发送数据
    if len(data_) > 0:
        client_socket.send(data_.encode('utf-8'))
    if data_ == 'exit':
        client_socket.close()
        break

    # 客户端接收数据
    data = client_socket.recv(1024)
    print(f'服务端127.0.0.1:{8888}:', data.decode('utf-8'))

client_socket.close()
