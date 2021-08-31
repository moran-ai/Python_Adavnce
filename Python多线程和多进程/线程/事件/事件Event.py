import threading
import time
import random

"""
门的状态有三种：
    ① 门已经打开,可以进入  0,1,2 打开
    ② 门已经关闭，需要刷卡进入  
    ③ 门自动关闭  3 关闭

人的状态有两种：
    ① 门打开，人可以直接进入
    ② 门关闭，需要刷卡
"""
# 设置一个事件
enevt = threading.Event()  # 默认为false
enevt.set()  # 设置一个标志位 门一开始就是打开的
# 设置一个状态  状态为打开
status = 0


def door():
    global status
    while True:
        print(f'当前门的状态是{status}')
        if status >= 3:
            print("门已经自动关闭")
            enevt.clear()
        if enevt.is_set():
            print("门已经打开，可以进入")
        else:
            print("门已经关闭，需要刷卡进入")
            enevt.wait()
            continue
        time.sleep(1)
        status += 1


def people():
    global status
    count = 0
    while True:
        count += 1
        if enevt.is_set():
            print(f'门开着,{count}号进入里面')
        else:
            print(f"门被关闭，{count}号刷卡进入")
            enevt.set()
            status = 0
        time.sleep(random.randint(1, 10))


if __name__ == '__main__':
    d = threading.Thread(target=door)
    p = threading.Thread(target=people)
    d.start()
    p.start()
