"""
@Author:hu
@Time:2021/9/1 15:26 
@File:线程事件实现红绿灯.py
@Software: PyCharm
"""
import threading, time
from threading import Event

"""
使用两个线程实现红绿灯，分别是汽车，红绿灯
"""
event = Event()

status = 0  # 记录红绿灯的状态


def car():
    """
    汽车
    :return:
    """
    count = 1  # 用来记录汽车的数量
    while True:
        if event.isSet():
            print('绿灯')
            print(f'{count}车通行')

        else:
            print('红灯，需要等待3秒')
            print('等待中...')
            event.wait()
            """
            如果标志位为False，则会调度到另一个线程,当前线程会进行阻塞
            如果标志位为True，当前线程则不会进行阻塞，继续向下执行
            """

        time.sleep(3)
        count += 1


def light():
    """
    红绿灯
    :return:
    """
    global status
    while True:
        print(f'当前状态是{status}')
        if status >= 3:
            print('红灯')
            event.clear()  # 将标志位置空为False
            status = 0

        else:
            # 否则就是绿灯
            event.set()

        time.sleep(5)
        status += 1


if __name__ == '__main__':
    t1 = threading.Thread(target=car)
    t2 = threading.Thread(target=light)
    t2.start()
    t1.start()
