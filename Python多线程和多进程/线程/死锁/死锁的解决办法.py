import time
from threading import *

# 使用while循环交叉执行，解决死锁的问题

lock1 = Lock()
lock2 = Lock()


class MyThread1(Thread):
    def run(self):
        while True:
            lock1.acquire()
            print('线程1获得了鱼')
            time.sleep(1)
            lock1.release()

            lock2.acquire()
            print('线程1获得了熊掌')
            time.sleep(1)
            lock2.release()


class MyThread2(Thread):
    def run(self):
        while True:
            lock2.acquire()
            print('线程2获得了熊掌')
            time.sleep(1)
            lock2.release()

            lock1.acquire()
            print('线程2获得了鱼')
            time.sleep(1)
            lock1.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
