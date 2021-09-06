"""
@Author:hu
@Time:2021/9/6 10:57 
@File:Pipe实现通信.py
@Software: PyCharm
"""
import os
import time
from multiprocessing import Pipe, Process

"""
使用生产者消费者的模式实现Pipe通信, 管道有两端
"""


class Product(Process):
    def __init__(self, name, p):
        super().__init__()
        self.name = name
        self.p = p

    def run(self) -> None:
        print(f'{self.name}, 进程{os.getpid()}启动')
        for i in range(10):
            self.p.send(i)
            time.sleep(1)
        print(f'{self.name}, 进程{os.getpid()}结束')


class Consumer(Process):
    def __init__(self, name, p):
        super().__init__()
        self.name = name
        self.p = p

    def run(self) -> None:
        print(f'{self.name}, 进程{os.getpid()}启动')
        while True:
            try:
                data = self.p.recv()
                print(data)
            except:
                break

        # 管道中没有数据，会一直进行阻塞，后面的代码不会执行


if __name__ == '__main__':
    p1, p2 = Pipe()
    p = Product('a', p1)
    c = Consumer('b', p2)
    p.start()
    c.start()
    p.join()

    # 消费者一直阻塞，需要杀死
    c.terminate()

    print('主线程结束')
