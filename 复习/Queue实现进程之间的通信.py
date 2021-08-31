# coding:utf-8
from multiprocessing import Process, Queue
import os, time


# 创建两个进程,一个负责读，另一个负责写
class Writeprocess(Process):
    def __init__(self, xname, mq):
        Process.__init__(self)
        self.name = xname
        self.mq = mq

    def run(self):
        # 把多条数据写入到队列中
        print('进程的名字:%s,ID:%s' % (self.name, os.getpid()))
        for i in range(1, 6):
            self.mq.put(i)  # writer进程负责把数据写入到队列中
            time.sleep(1)  # 休眠一秒钟
        print('进程的名字:%s,ID:%s,已经结束' % (self.name, os.getpid()))


class readprocess(Process):
    def __init__(self, xname, mq):
        Process.__init__(self)
        self.name = xname
        self.mq = mq

    def run(self):
        print('进程的名字:%s,ID:%s' % (self.name, os.getpid()))
        while True:
            # get函数是一个阻塞的函数
            value = self.mq.get(True)  # 当队列中没有数据，该行代码一直阻塞
            print(value)
            # 不会执行的代码
        print('进程的名字:%s,ID:%s,已经结束' % (self.name, os.getpid()))


if __name__ == '__main__':
    q = Queue()
    pw = Writeprocess('writer', q)
    pr = readprocess('read', q)
    # 启动两个进程
    pw.start()
    pr.start()
    # 让父进程等待子进程结束
    pw.join()
    # pr进程是一个死循环
    pr.terminate()
    print('父进程结束')
