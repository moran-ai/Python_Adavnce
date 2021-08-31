import time, random
from threading import *


def run():
    #  定义一个私有变量
    local_var = local()
    local_var.numbers = [1]  # 给定初始值为1
    # 给定休眠时间，模拟不同线程的执行
    time.sleep(random.random())
    for i in range(8):
        local_var.numbers.append(random.choice(range(10)))
    # 打印当前线程的私有变量值
    print(current_thread(), local_var.numbers)


if __name__ == '__main__':
    thread_list = []

    for i in range(5):
        t1 = Thread(target=run)
        t1.start()
        thread_list.append(t1)

    for j in thread_list:
        j.join()
