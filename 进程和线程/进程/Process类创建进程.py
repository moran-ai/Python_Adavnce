"""
@Author:hu
@Time:2021/9/6 10:15 
@File:Process类创建进程.py
@Software: PyCharm
"""
import multiprocessing
import time

"""
使用直接创建Process实例对象的方式创建进程
"""


def task():
    for i in range(10):
        print(f'当前进程是{multiprocessing.current_process()}--->', i)
        time.sleep(1)


if __name__ == '__main__':
    for i in range(3):
        p = multiprocessing.Process(target=task)
        p.start()
