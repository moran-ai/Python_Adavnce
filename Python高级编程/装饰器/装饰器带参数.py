import time
from functools import wraps


def logger(func):
    @wraps(func)
    def writer_logging(*args, **kwargs):
        print(f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}')
        func(*args, **kwargs)

    return writer_logging


@logger
def work():
    print('正在工作')


@logger
def work1(name):
    print(f'{name}在工作')


work()
work1('jk')
