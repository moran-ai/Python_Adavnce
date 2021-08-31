import os
import time
from multiprocessing import Process, Queue


# 创建两个进程，一个用于写，一个用来读
class WriterProcess(Process):
    def __init__(self, name, q):
        Process.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print(f'进程{self.name},ID{os.getpid()}已经启动')
        for i in range(1, 6):
            self.q.put(i)
            time.sleep(1)
        print(f'进程{self.name},ID{os.getpid()}已经结束')


class ReaderProcess(Process):
    def __init__(self, name, q):
        Process.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print(f'进程{self.name},ID{os.getpid()}已经启动')
        while True:
            # 读数据
            value = self.q.get(True)  # get()会阻塞
            print(value)
        # 队列中没有数据，会一直处于阻塞状态，后面的代码不会执行
        print(f'进程{self.name},ID{os.getpid()}已经结束')


if __name__ == '__main__':
    # 创建一个队列
    q = Queue()

    # 创建写进程
    pw = WriterProcess('writer', q)
    # 创建读进程
    pr = ReaderProcess('read', q)
    pw.start()
    pr.start()
    pw.join()
    # 杀死进程pr
    pr.terminate()
    print('父进程结束')
