"""
@Author:hu
@Time:2021/9/3 11:07 
@File:lock锁.py
@Software: PyCharm
"""
import threading
import time

"""
用多线程模拟购买电影票,出现的线程安全问题
"""
count = 100  # 票的个数
lock = threading.RLock()


def task():
    global count
    for i in range(1000):
        lock.acquire()
        if count > 0:
            print(f'{threading.current_thread().getName()}将第{count}张票售出')
            count -= 1
            time.sleep(0.1)
            lock.release()


ts = []

for i in range(5):
    t = threading.Thread(target=task)
    t.start()
