"""
@Author:hu
@Time:2021/9/6 11:40 
@File:Queue实现通信.py
@Software: PyCharm
"""
import time
import os
from multiprocessing import Queue, Process

"""
使用multiprocessing中的Queue进行通信，这个队列是操作系统开辟出来的一个空间，各个进程可以将数据存放到队列中
使用生产者消费者的模式实现通信
"""


class Product(Process):
    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q

    def run(self) -> None:
        print(f'{self.name}, 当前进程是{os.getpid()}')
        for i in range(10):
            self.q.put(i)
            time.sleep(1)
        print(f'{self.name}, 当期进程{os.getpid()}结束')


class Consumer(Process):
    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q

    def run(self) -> None:
        while True:
            try:
                print(f'{self.name}, 当前进程是{os.getpid()}')
                data = self.q.get(timeout=3)  # get方法会一直进行阻塞
                print(data)
            except:
                break

        # 队列中数据为空，会一直进行阻塞


if __name__ == '__main__':
    q = Queue()
    p = Product('a', q)
    c = Consumer('b', q)
    p.start()
    c.start()
    p.join()
