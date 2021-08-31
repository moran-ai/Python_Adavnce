# @Author:hu
# @Time:2021/8/30 14:15 
# @File:进程池.py
# @Software: PyCharm
import multiprocessing  # 进程模块
import psutil  # 获取系统进程信息
import os
from concurrent.futures import ProcessPoolExecutor  # 进程池

def task(max_num):
    """
    定义一个进程任务
    :param max_num:
    :return:
    """
    my_num = 0
    for i in range(max_num):
        pu = psutil.Process(os.getpid())
        print(f'当前进程名字为：{multiprocessing.current_process()}, id为：{pu.pid}')
        my_num += 1
    return my_num


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)
    for _ in range(4):
        pool.apply_async(task, (50,))

    pool.close()
    pool.join()


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as pool:
        pool.submit(task, 50)
        pool.submit(task, 60)
        pool.submit(task, 70)
        pool.submit(task, 80)
        pool.submit(task, 80)
        pool.submit(task, 80)
