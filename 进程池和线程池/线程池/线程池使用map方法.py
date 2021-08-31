# @Author:hu
# @Time:2021/8/30 13:48 
# @File:线程池使用map方法.py
# @Software: PyCharm
"""
线程池中的map方法会给可迭代对象中的每一个元素开启一个线程，并发的执行，相当于启动了len(可迭代对象)个线程
"""
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
        my_num += 1
    return my_num


with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(task, (50, 100, 40))
    print('--------------')
    for result in results:
        print('结果：', result)
