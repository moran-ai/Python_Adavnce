"""
@Author:hu
@Time:2021/9/4 14:55 
@File:队列通信.py
@Software: PyCharm
"""
import threading
import time
from queue import Queue


class Product(threading.Thread):
    """
    创建生产者
    """

    def __init__(self, q):
        """
        初始化实例属性
        :param q: 队列
        """
        super().__init__()
        self.q = q

    def run(self) -> None:
        count = 0
        while count < 100:
            try:
                if self.q.empty():
                    for i in range(100):
                        self.q.put(count)
                        count += 1
                        print(f'生产者生产了{count}个')
            except:
                break


class Consumer(threading.Thread):
    """
    创建消费者
    """

    def __init__(self, q):
        """
        初始化实例属性
        :param q:  队列
        """
        super().__init__()
        self.q = q

    def run(self) -> None:
        while True:
            try:
                num = self.q.get(timeout=3)
                print(f'消费者{threading.current_thread().getName()}拿到了第{num}个')
                time.sleep(1)
            except:
                break


if __name__ == '__main__':
    q = Queue()
    p = Product(q)
    p.start()

    for _ in range(1, 5):
        c = Consumer(q)
        c.start()
