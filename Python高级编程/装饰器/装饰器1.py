"""
装饰器的作用：给已经存在的函数添加额外的功能
"""
import time
from functools import wraps


def logger(func):
    @wraps(func)
    def writer_logging():
        print(f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}')
        func()

    return writer_logging


@logger
def work():
    print('正在工作')


work()

def hi():
    # 目标函数
    pass

def do(func):
    print('oooo')
    func()

do(hi)
