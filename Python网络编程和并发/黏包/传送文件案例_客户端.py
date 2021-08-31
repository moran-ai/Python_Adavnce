import struct
import os
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

# 给定文件的路径
file_path = '1.mp3'
# 以只读的方式打开这个文件
f = open('1.mp3', 'rb')

# 获取这个文件的大小
size = os.path.getsize(file_path)
# 准备一个报头 i占四个字节
header = struct.pack('!i', size)
# 发送这个报头
client.send(header)

# 发送文件内容
while True:
    data = f.read(1024)
    # 如果文件内容发送完毕，结束循环
    if not data:
        break
    client.send(data)

print('客户端发送完成')
f.close()
client.close()
