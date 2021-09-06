# @Author:hu
# @Time:2021/9/1 14:34 
# @File:线程事件Event.py
# @Software: PyCharm
"""
线程事件用于线程控制线程，控制多个进程之间的交互，线程事件的初始值为False
set:将线程事件的值设置为True
clear:将线程事件的值设置为False
"""
# import threading
# from threading import Event
#
#
# # 打印字母函数
# def printLetter(letterEvent, numEvent):
#     for item in ["a", "b", "c"]:
#         letterEvent.wait()
#         print(item, end=" ")
#         letterEvent.clear()
#         numEvent.set()
#
#
# # 打印数字函数
# def printNum(numEvent, letterEvent):
#     for item in [2, 4, 6]:
#         numEvent.wait()
#         print(item, end=" ")
#         numEvent.clear()
#         letterEvent.set()
#
#
# if __name__ == '__main__':
#     letterEvent, numEvent = Event(), Event()
#     t1 = threading.Thread(target=printLetter, args=(letterEvent, numEvent))
#     t2 = threading.Thread(target=printNum, args=(numEvent, letterEvent))
#
#     threads = []
#     threads.append(t1)
#     threads.append(t2)
#
#     for t in threads:
#         t.start()
#
#     letterEvent.set()
#     # numEvent.set()

"""
有两个线程A, B, A线程打印数字1,2,3,4,5,6 B线程打印字母a, b, c, d, e, f
要求得到最后的结果 a1 b2 c3...
"""
import threading
from threading import Event


def printLetter(letterEvent, numberEvent):
    """
    打印字母的线程
    :param letterEvent: 字母事件
    :param numberEvent: 数字事件
    :return:
    """
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f']
    for item in letter_list:
        letterEvent.wait()  # 进行阻塞，如果标志为True,则不需要进行阻塞
        print(item, end="")  # 进行打印
        letterEvent.clear()  # 清空标志，标志为False
        numberEvent.set()  # 设置另一个事件的标志为True


def printNumber(numberEvent, letterEvent):
    """
    打印数字线程
    :param numberEvent: 数字事件
    :param letterEvent: 字母事件
    :return:
    """
    number_list = [1, 2, 3, 4, 5, 6]
    for item in number_list:
        numberEvent.wait()
        print(item, end=" ")
        numberEvent.clear()
        letterEvent.set()


if __name__ == '__main__':
    # 创建两个事件
    letter_Event, number_Event = Event(), Event()

    threads = []
    thread1 = threading.Thread(target=printLetter, args=(letter_Event, number_Event))
    thread2 = threading.Thread(target=printNumber, args=(number_Event, letter_Event))
    threads.append(thread1)
    threads.append(thread2)

    for i in threads:
        i.start()

    letter_Event.set()
    # number_Event.set()
