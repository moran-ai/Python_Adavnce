import socket

# 创建套接字  TCP协议
"""
参数：
    第一个参数：
      address family:  AF_INET(常用) 用于Internet之间的通信  AF_UNIX 用于同一台机器之间的进程通信
    第二个参数：
        Type:套接字类型 
            SOCK_STREAM  流式套接字，用于TCP协议
            SOCK_DGRAM   数据报套接字 用于UDP协议
"""
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s1)
# UDP协议
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
