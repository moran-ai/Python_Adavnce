# @Author:hu
# @Time:2021/9/1 13:40 
# @File:schedule类.py
# @Software: PyCharm
"""
schedule类可以用来执行更加复杂的任务调度
"""
import threading
from sched import scheduler


def action(arg):
    """
    要运行的函数
    :param arg:
    :return:
    """
    print(arg)


def thread_action(*add):
    """
    线程需要运行的函数
    :param add: *add可以接收多个非关键字形式的参数,使用*进行解包
    :return:
    """
    # 创建任务调度对象，并进行接收
    sche = scheduler()

    # 定义优先级  优先级越大，数字越小
    i = 3
    for a in add:
        # 调用enter方法，enter(时间, 优先级, 目标函数, 函数参数)
        sche.enter(1, i, action, argument=(a,))
        i -= 1
    sche.run()  # 调度所有的任务


# 线程参数
args = (
    '1', '2', '3'
)
# 创建线程
thread = threading.Thread(target=thread_action, args=args)
thread.start()
