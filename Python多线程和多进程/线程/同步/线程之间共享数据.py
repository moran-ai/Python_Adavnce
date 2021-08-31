import time
from threading import Thread

num = 0


def run1():
    global num
    for _ in range(10):
        num += 1
    print(f'线程一的num值是{num}')


def run2():
    global num
    print(f'线程二的num值是{num}')


if __name__ == '__main__':
    t1 = Thread(target=run1)
    t2 = Thread(target=run2)
    t1.start()
    time.sleep(1)
    t2.start()
    print('主线程结束')
