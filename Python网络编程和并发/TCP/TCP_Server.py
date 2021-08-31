from socket import *

# 创建一个套接字 SOCK_STREAM用于TCP
server_socket = socket(AF_INET, SOCK_STREAM)

# 绑定IP和端口
server_socket.bind(('', 8080))

# 服务器的socket监听，listen让Socket处于被动  5代表客户端处理的线程
server_socket.listen(5)

# 等待客户端的链接请求 【TCP是面向链接的协议】  返回两个值，一个是新的socket,一个是客户端的ip地址
new_socket, client_addr = server_socket.accept()  # 阻塞函数

# 服务端接收客户端发送过来的请求
data = new_socket.recv(1024)
print('服务器接收的数据是:', data.decode('utf-8'))

# 服务端发送数据给客户端
# new_socket.send('thank you'.encode('utf-8'))
new_socket.send(data)

# 关闭socket
new_socket.close()  # 当前客户端的socket关闭
server_socket.close()  # 整个服务器的socket关闭
