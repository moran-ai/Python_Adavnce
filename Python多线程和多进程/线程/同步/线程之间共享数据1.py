import time
from threading import Thread


def run1(num):
    for _ in range(10):
        num[0] += 1
    print(f'线程一的num值是{num[0]}')


def run2(num):
    print(f'线程二的num值是{num[0]}')


if __name__ == '__main__':
    i = [0]  # 为了让多个线程可以共享数据，需要使用可变类型
    t1 = Thread(target=run1, args=(i,))
    t2 = Thread(target=run2, args=(i,))
    t1.start()
    time.sleep(1)
    t2.start()
    print(f'全局变量i的值是{i}')
    print('主线程结束')
