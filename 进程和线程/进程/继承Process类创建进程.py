"""
@Author:hu
@Time:2021/9/6 10:29 
@File:继承Process类创建进程.py
@Software: PyCharm
"""
import multiprocessing
import time
import os

"""
继承Process类创建进程
"""


class MyProcess(multiprocessing.Process):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        """
        重写run方法
        :return:
        """
        for i in range(10):
            print(f'当前进程为{os.getpid()}--->', i)
            time.sleep(3)


if __name__ == '__main__':
    for i in range(5):
        p = MyProcess()
        p.start()
