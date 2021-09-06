"""
@Author:hu
@Time:2021/9/4 11:26 
@File:死锁.py
@Software: PyCharm
"""
import threading
import time
from contextlib import contextmanager

"""
当多个线程互相持有对方拥有的资源时，并且都不释放资源，这样就会导致死锁，会永久阻塞下去
"""

# 用来存储local的数据
_local = threading.local()


@contextmanager
def acquire(*locks):
    # 对锁按照id进行排序
    locks = sorted(locks, key=lambda x: id(x))

    # 如果已经持有锁当中的序号有比当前更大的，说明策略失败
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # 获取所有锁
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # 倒叙释放
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('thread-1')


def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('thread-2')


# t1 = threading.Thread(target=thread_1)
# t1.start()
#
# t2 = threading.Thread(target=thread_2)
# t2.start()

# 线程交叉执行解决死锁

def thread1():
    while True:
        x_lock.acquire()
        print('线程1获得锁1')
        x_lock.release()
        time.sleep(1)

        y_lock.acquire()
        print('线程1获得锁2')
        y_lock.release()
        time.sleep(1)


def thread2():
    while True:
        while True:
            y_lock.acquire()
            print('线程2获得锁2')
            y_lock.release()
            time.sleep(1)

            x_lock.acquire()
            print('线程2获得锁1')
            x_lock.release()
            time.sleep(1)


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()
