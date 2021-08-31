import time
import threading
import wx
from socket import *


class MySever(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=102, title='jk的服务端', pos=wx.DefaultPosition, size=(400, 470))
        # 初始化一个面板
        p = wx.Panel(self)
        # 创建一个盒子，用来存放文本框
        box = wx.BoxSizer(wx.VERTICAL)  # VERTICAL 垂直居中

        # 创建一个网格，用来存放按钮
        g = wx.FlexGridSizer(wx.HORIZONTAL)  # HORIZONTAL:水平方向
        # 创建三个按钮，用来开启服务器，保存聊天记录，断开服务器
        start_server_button = wx.Button(p, size=(133, 40), label='启动')
        recored_save_button = wx.Button(p, size=(133, 40), label='保存聊天记录')
        stop_server_button = wx.Button(p, size=(133, 40), label='断开')
        g.Add(start_server_button, 1, wx.Top)
        g.Add(recored_save_button, 1, wx.Top)
        g.Add(stop_server_button, 1, wx.Top)
        box.Add(g, 1, wx.ALIGN_CENTER)

        # 创建可读的文本框
        self.text = wx.TextCtrl(p, size=(400, 400), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTER)

        # 盒子放入面板中
        p.SetSizer(box)

        # 设定服务器的属性
        self.isOn = False  # 服务器没有启动
        self.host_port = ('', 8888)  # 服务器的ip地址
        self.server_socket = socket(AF_INET, SOCK_STREAM)  # TCP的套接字
        self.server_socket.bind(self.host_port)  # 绑定ip
        self.server_socket.listen(5)  # 服务器主动变被动
        self.session_thread_map = {}  # 字典存放所有的服务器会话线程  客户端名字为key,会话线程为value

        # 给所有的按钮绑定事件
        # 给启动按钮绑定一个事件，事件触发时会调用一个函数
        self.Bind(wx.EVT_BUTTON, self.start_server, start_server_button)
        self.Bind(wx.EVT_BUTTON, self.record_save, recored_save_button)
        self.Bind(wx.EVT_BUTTON, self.stop_server, stop_server_button)

    def start_server(self, event):
        """
        开启服务器
        :param event:
        :return:
        """
        print('服务器开始启动')
        if not self.isOn:
            # 启动服务器的主线程
            self.isOn = True
            # 创建线程
            main_thread = threading.Thread(target=self.do_work)
            # 设置守护线程
            main_thread.setDaemon(True)
            main_thread.start()

    def do_work(self):
        """
        服务器工作
        :return:
        """
        print('服务器开始工作')
        while self.isOn:
            # 建立连接
            session_socket, client_add = self.server_socket.accept()
            # 获取客户端的名字
            username = session_socket.recv(1024).decode('utf-8')
            # 创建会话线程
            session_thread = SessionThread(session_socket, username, self)
            # 会话线程交给服务器进行管理
            self.session_thread_map[username] = session_thread
            # 会话线程开启
            session_thread.start()
            # 表示有客户端进入聊天室
            self.show_info_and_send_client('服务器通知', f'欢迎{username}进入聊天室',
                                           time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        self.server_socket.close()

    def show_info_and_send_client(self, source, data, data_time):
        """
        发送数据
        :param source: 信息的来源
        :param data: 数据
        :param data_time: 时间
        :return:
        """
        # 发送的数据
        send_data = f'{source}: {data}\n{data_time}'
        # 在服务器显示文本信息
        self.text.AppendText(f'----------------------\n{send_data}')
        # 发送给所有的客户端 所有的客户端由会话线程进行管理
        for client in self.session_thread_map.values():
            # 如果当前线程是正在运行状态，则发送
            if client.isOn:
                client.user_socket.send(send_data.encode('utf-8'))

    def record_save(self, event):
        """
        保存聊天记录
        :param event:
        :return:
        """
        record = self.text.GetValue()
        with open('record.txt', 'w+') as f:
            f.write(record)

    def stop_server(self, evnet):
        print('服务器断开')
        if self.isOn:
            self.show_info_and_send_client('服务器通知', '服务器已断开',
                                           time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            self.isOn = False


class SessionThread(threading.Thread):
    def __init__(self, user_socket, username, server):
        """
        会话线程
        :param user_socket: 套接字
        :param username: 客户端的名字
        :param server: 服务器
        """
        threading.Thread.__init__(self)
        self.user_socket = user_socket
        self.username = username
        self.server = server
        self.isOn = True  # 会话线程是否启动

    def run(self):
        print(f'客户端{self.username}连接服务器成功，服务器启动一个会话线程')
        while self.isOn:
            # 接受客户端的聊天信息
            data = self.user_socket.recv(1024).decode('utf-8')
            # 如果客户端点击断开按钮，先发一条消息给客户端，消息的内容规定为A^disconnect^B
            if data == 'A^disconnect^B':
                self.isOn = False
                self.server.show_info_and_send_client('服务器通知', f'{self.username}离开聊天室',
                                                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            else:
                # 其他聊天信息，展示给服务器和客户端
                self.server.show_info_and_send_client(self.username, data,
                                                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        # 保持和客户端会话的socket关闭
        self.user_socket.close()


if __name__ == '__main__':
    app = wx.App()
    MySever().Show()
    app.MainLoop()
