import os
import time
import random
from multiprocessing import Process
from multiprocessing.pool import Pool


def run(name):
    start = time.time()
    print(f'进程{name}已经启动，ID{os.getpid()}')
    time.sleep(random.choice([1, 2, 3, 4, 5]))
    end_time = time.time() - start
    print(f'进程{name}已经结束，ID{os.getpid()},耗时{end_time}')


if __name__ == '__main__':
    # 创建一个进程池
    p = Pool(5)
    for i in range(10):
        p.apply_async(run, (f'process{i}',))
    p.close()
    p.join()
    print('主进程结束')
