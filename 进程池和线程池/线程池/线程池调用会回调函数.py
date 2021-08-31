# @Author:hu
# @Time:2021/8/30 12:17 
# @File:线程池调用会回调函数.py
# @Software: PyCharm
import time
import threading
from concurrent.futures import ThreadPoolExecutor


def task(max_num):
    """
    定义一个线程任务
    :param max_num:
    :return:
    """
    my_num = 0
    for i in range(max_num):
        print(threading.current_thread().getName() + ' ' + str(i))
        my_num += i
    return my_num


# 使用上下文管理创建线程池
with ThreadPoolExecutor(max_workers=4) as pool:
    # 提交任务到线程池
    future1 = pool.submit(task, 50)
    future2 = pool.submit(task, 100)


    # 定义一个回调函数
    def get_result(future):
        print(future.result())


    # 为future1添加回调函数
    future1.add_done_callback(get_result)
    print('----------------------')
    future2.add_done_callback(get_result)
