import time
from threading import *

lock1 = Lock()
lock2 = Lock()
# lock3 = Lock()  Lock是互斥锁
lock3 = RLock()  # 使用逻辑锁 只针对一个线程


class MyThread1(Thread):
    def run(self):
        lock1.acquire()
        print('线程1获得了lock1')
        time.sleep(1)
        lock2.acquire()
        print('线程1获得了lock2')
        lock1.release()
        lock2.release()


class MyThread2(Thread):
    def run(self):
        lock2.acquire()
        print('线程2获得了lock2')
        time.sleep(1)
        lock1.acquire()
        print('线程2获得了lock1')
        lock2.release()
        lock1.release()

class MyThread3(Thread):
    def run(self):
        lock3.acquire()
        print('线程3获得lock3')
        time.sleep(1)
        self.run()
        lock3.release()

if __name__ == '__main__':
    # t1 = MyThread1()
    # t2 = MyThread2()
    # t1.start()
    # t2.start()
    t3 = MyThread3()
    t3.start()
