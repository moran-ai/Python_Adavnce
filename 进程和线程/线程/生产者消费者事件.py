"""
@Author:hu
@Time:2021/9/2 14:24 
@File:生产者消费者事件.py
@Software: PyCharm
"""
import time
from threading import Thread, Event

"""
使用消费者和生产者模式实现事件
"""

x = 0


class Product(Thread):
    def __init__(self, couster):
        super().__init__()
        self.couster = couster

    def run(self) -> None:
        """
        重写run方法，生产者对x进行乘积，共10次
        :return:
        """
        global x
        for i in range(0, 10):
            x = i ** 2
            self.couster.work()  # 唤醒消费者线程
            time.sleep(1)


class Coumter(Thread):
    def __init__(self):
        super().__init__()
        self.event = Event()

    def work(self):
        self.event.set()

    def run(self) -> None:
        global x
        count = 10
        while count > 0:
            self.event.wait()  # 消费者线程阻塞，调度到生产者
            self.event.clear()  # 将标志重置为False
            print(x)
            count -= 1


if __name__ == '__main__':
    c = Coumter()
    c.start()
    Product(c).start()
