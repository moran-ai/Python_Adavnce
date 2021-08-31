from socket import *

# 创建客户端的socket  遵循UDP协议
client_socket = socket(AF_INET, SOCK_DGRAM)

# 确定目标服务器的ip和端口
host_port = ("127.0.0.1", 8080)

# 输入内容  对内容进行编码 转为bytes数据
data = input("请输入:").encode('utf-8')

# 发送消息
client_socket.sendto(data, host_port)

# 关闭socket
client_socket.close()