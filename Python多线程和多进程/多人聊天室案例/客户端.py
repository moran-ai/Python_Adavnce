import threading
import wx
from socket import *


# 创建一个客户端界面 需要继承父类wx.Frame 就拥有了界面
class MyClient(wx.Frame):
    def __init__(self, name):  # name:客户端的名字
        self.name = name
        self.isConnect = False  # 客户端是否连接服务器
        self.client_scoket = None  # 客户端的socket
        wx.Frame.__init__(self, None, id=101, title=f'{name}的客户端', pos=wx.DefaultPosition, size=(400, 470))
        # 在窗口中初始化一个面板
        p = wx.Panel(self)
        # 在面板里面添加按钮，文本框，文本输入框，把这些对象都放到一个盒子里面
        box = wx.BoxSizer(wx.VERTICAL)  # VERTICAL:盒子里面垂直方向自动排版

        g1 = wx.FlexGridSizer(wx.HORIZONTAL)  # v:可伸缩的网格布局，HORIZONTAL:水平方向
        # 创建两个按钮，一个用来连接，一个用来断开
        conn_button = wx.Button(p, size=(200, 40), label='连接')
        dis_conn_button = wx.Button(p, size=(200, 40), label='断开')
        # 将按钮添加到水平布局
        g1.Add(conn_button, 1, wx.Top | wx.LEFT)  # 连接按钮布局在左上
        g1.Add(dis_conn_button, 1, wx.Top | wx.RIGHT)  # 断开按钮布局在右上
        # 联合居中
        box.Add(g1, 1, wx.ALIGN_CENTER)  # ALIGN_CENTER:联合居中

        # 创建一个网格  水平布局
        g2 = wx.FlexGridSizer(wx.HORIZONTAL)
        # 创建聊天界面的文本框，只读
        self.text = wx.TextCtrl(p, size=(400, 250), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTER)  # 放入盒子中，联合居中

        # 创建聊天界面的输入框  可写可读
        self.input_text = wx.TextCtrl(p, size=(400, 100), style=wx.TE_MULTILINE)
        box.Add(self.input_text, 1, wx.ALIGN_CENTER)

        # 在底部创建两个按钮 一个是重置，一个是发送
        clear_button = wx.Button(p, size=(200, 40), label='重置')
        send_button = wx.Button(p, size=(200, 40), label='发送')
        # 将按钮添加到水平布局
        g2.Add(clear_button, 1, wx.Top | wx.LEFT)
        g2.Add(send_button, 1, wx.Top | wx.RIGHT)
        # 联合居中
        box.Add(g2, 1, wx.ALIGN_CENTER)
        p.SetSizer(box)  # 盒子放入面板中

        # 给所有按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.connect_server, conn_button)
        self.Bind(wx.EVT_BUTTON, self.send_to_server, send_button)
        self.Bind(wx.EVT_BUTTON, self.go_out, dis_conn_button)
        self.Bind(wx.EVT_BUTTON, self.clear, clear_button)

    def connect_server(self, event):
        """
        客户端连接服务器
        :param event:
        :return:
        """
        print(f'客户端{self.name}开始连接')
        if not self.isConnect:
            # 服务器的ip地址
            host_port = ('127.0.0.1', 8888)
            # 创建客户端的socket
            self.client_scoket = socket(AF_INET, SOCK_STREAM)
            # 客户端连接服务器
            self.client_scoket.connect(host_port)
            # 将客户端的名字发送给服务器
            self.client_scoket.send(self.name.encode('utf-8'))
            t = threading.Thread(target=self.recive_data)
            t.setDaemon(True)
            self.isConnect = True
            t.start()

    def recive_data(self):
        print('客户端准备接收服务器的数据')
        # 如果客户端是连接的状态
        while self.isConnect:
            # 接收服务器发送过来的数据
            data = self.client_scoket.recv(1024).decode('utf-8')
            # 将服务器发送过来的数据展示在文本框上
            self.text.AppendText(f'\n{data}')

    def send_to_server(self, event):
        """
        客户端连接服务器
        :param event:
        :return:
        """
        if self.isConnect:
            info = self.input_text.GetValue()
            if info != '':
                self.client_scoket.send(info.encode('utf-8'))
                # 文本框中的内容发送以后，需要清空
                self.input_text.SetValue('')

    def go_out(self, event):
        """
        客户端离开
        :param event:
        :return:
        """
        self.client_scoket.send('A^disconnect^B'.encode('utf-8'))
        # 客户端断开连接
        self.isConnect = False

    def clear(self, event):
        """
        客户端清空输入框的内容
        :param event:
        :return:
        """
        self.input_text.Clear()


if __name__ == '__main__':
    app = wx.App()
    name = input('输入客户端名：')
    MyClient(name).Show()
    app.MainLoop()  # 循环刷新展示
