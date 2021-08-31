import time
import os
from multiprocessing import Pool


def test1():
    print(f'当前进程id是{os.getpid()},父进程id是{os.getppid()}')
    print('起床')
    time.sleep(3)
    return 'abc'


def test2():
    print(f'开始早读,当前进程id是{os.getpid()}')
    time.sleep(5)
    print('早读完成')


def test3(args):
    """
    test3是test1和test2执行完毕后才会执行
    :return:
    """
    print(f'吃早餐,当前进程idhi是{os.getpid()}')
    print(f'参数是{args}')
    print('早餐吃完')

if __name__ == '__main__':
    po = Pool(4)
    # 异步
    po.apply_async(func=test1, callback=test3)
    test2()
