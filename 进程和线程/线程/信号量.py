"""
@Author:hu
@Time:2021/9/5 9:18 
@File:信号量.py
@Software: PyCharm
"""
import time
import threading

"""
信号量可以用来控制并发线程的个数
Python多线程中有两种内置的信号量，信号量是通过内置的计数器对线程进行记录
BoundedSemaphore
Semaphore
调用acquire计数器减1，调用release计数器加1
BoundedSemaphore和Semaphore的区别：
    BoundedSemaphore如果调用时计数器的值超过了初始值会抛出异常，Semaphore不会抛出
"""
# 创建一个信号量
sem = threading.Semaphore(5)


# 创建一个函数，每次用5个线程打印打印当前时间
def task():
    sem.acquire()  # 加锁
    time.sleep(3)
    print(time.ctime())
    sem.release()  # 释放锁


if __name__ == '__main__':
    for i in range(20):
        t = threading.Thread(target=task)
        t.start()
        t.join()
