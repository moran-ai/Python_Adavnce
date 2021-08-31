import time
from functools import wraps


class Logger:
    def __init__(self, log_file='work.txt', level='INFO'):
        self.log_file = log_file
        self.level = level

    def __call__(self, func):
        @wraps(func)
        def logger(*args, **kwargs):
            log = f'{[self.level]}------> 时间是:{time.strftime("%H:%M:%S", time.localtime())}'
            print(log)
            with open(self.log_file, 'a') as f:
                f.write(log)
            func(*args, **kwargs)

        return logger


@Logger()
def work():
    print('工作')


@Logger(log_file='work1.txt', level='WARING')
def work1():
    print('共')


work()
work1()
