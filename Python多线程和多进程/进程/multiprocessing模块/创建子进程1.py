import os
import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print('当前进程的id', os.getpid())
        print('当前父进程的id', os.getppid())
        print('当前进程的名字', self.name)
        time.sleep(3)


if __name__ == '__main__':
    start = time.time()
    process_list = []
    for i in range(10):
        process_ = MyProcess(f'进程名是：{i + 1}')
        process_.start()
        process_list.append(process_)

    for ii in process_list:
        # 阻塞 父进程等待所有的子进程结束，才会执行后面的代码
        ii.join()

    #所有子进程结束才会执行
    end_time = time.time() - start
    print(end_time)
