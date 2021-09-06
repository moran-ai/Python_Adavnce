"""
@Author:hu
@Time:2021/9/4 13:20 
@File:装饰器的方式创建上下文.py
@Software: PyCharm
"""
"""
yield前面的相当于enter,后面的相当于exit
"""
import time
from contextlib import contextmanager


@contextmanager
def timethis(lable):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'{lable}:{end - start}')


with timethis('timer'):
    pass
