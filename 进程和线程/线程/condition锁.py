"""
@Author:hu
@Time:2021/9/3 15:35 
@File:condition锁.py
@Software: PyCharm
"""
import threading
import time

"""
使用condition锁实现生产者和消费者模式，用来模拟商品的生成和出售
使用一个生产者，多个消费者
生产者生成10个商品后，生产者生产期间不能进行购买，生产10个以后，停止生产，通知消费者购买
消费者收到了通知进行购买，当商品小于0个时，消费者通知生产者进行购买

condition锁类似于Event事件，只不过condition带上了锁
"""

num = 0  # 商品的数量
con = threading.Condition()  # 创建Condition锁对象


class Product(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        global num
        # 加锁
        con.acquire()
        while True:
            num += 1  # 生产商品
            print(f'生产者生产了{num}个商品')
            time.sleep(1)
            # 生产者生产10个商品后，通知消费者进行购买
            if num >= 10:
                print('已经生产10个，不再进行生产')
                # 通知消费者
                con.notify()
                con.wait()  # 消费者收到消费后，重新获取锁
        con.release()  # 释放锁


class Consumer(threading.Thread):
    def __init__(self, money):
        super().__init__()
        self.money = money

    def run(self) -> None:
        global num
        # 判断消费者是否有钱
        while self.money > 0:
            """
            这个地方的锁加在循环里面，是因为一个消费者购买完成之后释放锁，其他消费者可以立即进行购买
            如果放在循环外面，那么整个循环都会被一个循环锁住，其他消费者无法进行购买
            """
            con.acquire()  # 加锁
            if num <= 0:
                print(f'{threading.current_thread().getName()}通知生产者，没有货了')
                con.notify()  # 通知消费者
                con.wait()  # 释放锁 进行阻塞
            self.money -= 1
            num -= 1
            print(f'{threading.current_thread().getName()}消费了1个, 还剩{num}个')
            con.release()  # 释放锁
            time.sleep(1)
        print(f'{threading.current_thread().getName()}余额不够，无法消费')


if __name__ == '__main__':
    p1 = Product()
    c1 = Consumer(10)
    c2 = Consumer(10)
    c3 = Consumer(10)
    p1.start()
    c1.start()
    c2.start()
    c3.start()
    c1.join()
    c2.join()
    c3.join()
