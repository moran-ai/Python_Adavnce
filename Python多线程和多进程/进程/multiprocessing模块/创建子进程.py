import time
import os
from multiprocessing import Process

def test(name):
    print('当前进程的id', os.getpid())
    print('当前父进程的id', os.getppid())
    print('当前进程的名字', name)

    time.sleep(3)

if __name__ == '__main__':
    for i in range(10):
        process_ = Process(target=test, args=(f'进程id是{i}',))
        process_.start()

    print('父进程执行完毕')
    # 父进程中没有任何阻塞的代码，父进程必须等待所有子进程执行完毕后才结束
