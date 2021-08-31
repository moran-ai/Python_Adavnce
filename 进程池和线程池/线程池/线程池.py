"""
Python中使用concurrent.futures中的ThreadPoolExecutor来创建线程池
线程池创建的步骤：
    ① 调用ThreadPoolExecutor函数来创建一个线程池
    ② 定义一个普通函数作为任务
    ③ 调用ThreadPoolExecutor对象中的submit()方法将线程任务提交到线程池
    ④ 不想提交线程任务，调用ThreadPoolExecutor对象中的shutdown()方法关闭线程池
"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def task(max_sum):
    """
    定义一个线程任务函数
    :return:
    """
    my_sum = 0
    for i in range(max_sum):
        print(threading.current_thread().getName() + ' ' + str(i))
        my_sum += 1
    return my_sum


if __name__ == '__main__':
    # 创建线程池  包含4个线程
    pool = ThreadPoolExecutor(max_workers=4)

    # 向线程池中提交任务  调用submit方法
    future1 = pool.submit(task, 50)  # submit方法会返回一个future对象 这个future对象代表的是将来要执行的任务

    # 向线程池中再次提交一个任务
    future2 = pool.submit(task, 100)

    # 判断任务是否执行完成 使用done方法  如果执行完成，返回True
    print(future1.done())
    print('------------------')
    time.sleep(3)
    print(future2.done())

    # 查看线程任务返回的结果
    print(future1.result())
    print('*************************')
    print(future2.result())

    # 关闭线程池
    pool.shutdown()
