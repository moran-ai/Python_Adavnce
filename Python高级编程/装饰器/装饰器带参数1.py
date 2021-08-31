import time
from functools import wraps


def main_logger(logfile='work.log'):
    def logger(func):
        @wraps(func)
        def writer_logging(*args, **kwargs):
            log = f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}'
            print(log)
            with open(logfile, 'a') as f:
                f.write(log)
            func(*args, **kwargs)

        return writer_logging

    return logger


@main_logger()
def work():
    print('正在工作')


@main_logger('log1.log')
def work1(name):
    print(f'{name}在工作')


work()
work1('jk')
