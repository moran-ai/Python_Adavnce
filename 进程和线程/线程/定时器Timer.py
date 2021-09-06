# @Author:hu
# @Time:2021/9/1 12:14 
# @File:定时器Timer.py
# @Software: PyCharm
import time
from threading import Timer


def hello():
    print('Hello Word')


t = Timer(8, hello)
t.start()

count = 0


def hello1():
    print(time.time())
    global t, count
    count += 1
    if count < 10:
        t = Timer(1, hello1)
        t.cancel()  # 取消调度
        t.start()


t = Timer(1, hello1)
t.start()
