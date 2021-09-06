"""
@Author:hu
@Time:2021/9/2 13:17 
@File:线程事件实现开门和关门.py
@Software: PyCharm
"""
import threading
import time

"""
线程A实现关门
线程B表示员工
"""
# event = threading.Event()
# event1 = threading.Event()
#
#
# # status = 0  # 记录门的状态
# #
# #
# # def door():
# #     """
# #     门有三种状态:
# #         ① 自动关门
# #         ② 限时关门
# #         ③ 开门
# #     :return:
# #     """
# #     global status
# #     while True:
# #         if status >= 3:
# #             print('门已经自动关闭')
# #             event.clear()  # 将标志设置为False
# #             status = 0
# #
# #         if event.isSet():
# #             # 门开着
# #             print('门开着，可以进去')
# #
# #         # 门已经关闭
# #         else:
# #             print('门已经关闭，刷卡进去')
# #             event.wait()  # 当前线程阻塞，调度到另一个线程
# #         time.sleep(3)
# #         status += 1
# #
# #
# # def people():
# #     """
# #     ① 门开着，直接进去
# #     ② 门关着，刷卡进去
# #     :return:
# #     """
# #     global status
# #     count = 0
# #     while True:
# #         if event.isSet():
# #             print(f'门开着,{count}进入')
# #
# #         else:
# #             print(f'门关闭，{count}刷卡进去')
# #             event.set()
# #         time.sleep(3)
# #         count += 1
# #
# #
# # t1 = threading.Thread(target=door)
# # t2 = threading.Thread(target=people)
# # t1.start()
# # t2.start()
# # event = threading.Event()
#
#
# def printleeter():
#     """
#     打印字母
#     :return:
#     """
#     for item in [1, 2, 3, 4, 5, 6]:
#         event.wait()
#         print(item, end='')
#         event.clear()
#         event1.set()
#
#
# def printnumber():
#     """
#     打印数字
#     :return:
#     """
#     for item in ['a', 'b', 'c', 'd', 'e', 'f']:
#         event1.wait()
#         print(item, end=' ')
#         event1.clear()
#         event.set()
#
#
# t1 = threading.Thread(target=printleeter)
# t2 = threading.Thread(target=printnumber)
# t1.start()
# t2.start()
# event.set()

from threading import Thread, Event
import time

x = 0


class Producer(Thread):
    def __init__(self, consumer):
        Thread.__init__(self)
        self.consumer = consumer

    def run(self):
        global x
        for i in range(0, 10):
            x = i ** 2
            self.consumer.wake()
            time.sleep(1)


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.event = Event()

    def wake(self):
        # 设置标志位（置为True）
        self.event.set()

    def run(self):
        global x
        count = 10
        while count > 0:
            # 阻塞等待直到标志位被置为True
            self.event.wait()
            # 清除标志位(置为False)，为下次阻塞等待做准备
            self.event.clear()
            print('Consumer:', time.time(), 'x=', x)
            count -= 1


if __name__ == '__main__':
    c = Consumer()
    c.start()
    Producer(c).start()
