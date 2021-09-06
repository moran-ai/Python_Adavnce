"""
@Author:hu
@Time:2021/9/2 12:03 
@File:线程事件实现餐馆消费.py
@Software: PyCharm
"""
import threading
import time

"""
使用线程事件实现餐馆消费
线程A: 顾客
线程B：食物
"""
# 创建一个事件
event = threading.Event()
status = 0  # 用来记录食物的状态


def customer():
    """
    顾客线程,顾客需要进行消费
    :return:
    """
    global status
    count = 0  # 记录顾客
    while True:
        if event.isSet():
            print(f'{count}号顾客取餐')

        else:
            print('食物正在制作当中，请等待...')
            print('*****>', status)  # 0
            event.wait()  # 阻塞当前线程，去执行另一个线程
        time.sleep(3)
        count += 1


def food():
    """
    食物线程
    :return:
    """
    global status
    while True:
        if status >= 3:
            event.clear()  # 当前标志位设置为False 去执行另一个线程
            print(f'当前食物的状态是{status}--->{event.isSet()}')
            print('=====>', status)
            status = 0
            continue

        else:
            print('食物完成，顾客可以取餐')
            event.set()
            print(f'当前食物的状态是{status}--->{event.isSet()}')
        time.sleep(5)
        status += 1
        print('食物:', status)


t1 = threading.Thread(target=food)
t2 = threading.Thread(target=customer)
t1.start()
t2.start()
