# @Author:hu
# @Time:2021/8/31 14:52 
# @File:线程.py
# @Software: PyCharm
"""
线程创建的方式
① 直接使用threading模块中的Thread类创建
② 继承threading模块中的Thread类创建一个派生类，创建派生类的实例对象
线程的方法：
    setName:设置线程名字
    getName:获取线程名字
    isAlive:判断线程是否是活动的  该方法已弃用
    is_alive:判断线程是否是活动的
"""
import threading
import time

lock = threading.Lock()


# 方式一创建
def task(num):
    """
    目标函数
    :param num:
    :return:
    """
    n = 0
    for i in range(num):
        lock.acquire()  # 加锁
        print(f'当前线程是{threading.current_thread().getName()}, {n}')
        n += 1
        lock.release()  # 释放锁


if __name__ == '__main__':
    threads = []
    # for i in range(5):
    #     thread = threading.Thread(target=task, args=(40,))
    #     thread.setDaemon(True)
    #     thread.start()
    #     time.sleep(1)
    #     thread.join()
    # print('MainThread')
    for i in range(5):
        thread = threading.Thread(target=task, args=(1,))  # 调用threading中的Thread创建线程
        threads.append(thread)

    for i in range(5):
        threads[i].start()  # 线程由新建状态进入就绪状态，该方法每个线程只会调用一次，多次调用会抛出RuntimeError异常
        time.sleep(1)  # 休眠1秒

    for i in range(5):
        threads[i].join()  # 进行阻塞 指定线程占用CPU的时间，默认是从线程创建到死亡的时间

    print('MainThreadFinish')  # 主线程结束
