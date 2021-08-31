import gevent
import time
from gevent import monkey


def task1(name):
    for i in range(5):
        print(name, i)
        time.sleep(1)


def task2(name):
    for i in range(5):
        print(name, i)
        time.sleep(1)


# if __name__ == '__main__':
#     monkey.patch_all()  # 给所有耗时操作打上补丁
#
#     gevent.joinall([  # 将所有协程添加到事件循环
#         gevent.spawn(task1, 'a'),  # 创建协程
#         gevent.spawn(task2, 'b')
#     ])
#     print('this is main thread')
import random
random.randint(1,20)
