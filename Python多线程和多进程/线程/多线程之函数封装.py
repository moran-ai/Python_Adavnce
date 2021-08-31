import threading
import time, os


def run(name):
    for i in range(3):
        print(f'线程名字{name},输出:{i}')
        time.sleep(1)


if __name__ == '__main__':
    print(f'主线程开始时间{time.time()}')
    s = 'abcdef'
    for i in range(5):
        thread_t = threading.Thread(target=run, args=(s[i]))
        thread_t.start()
    print('主线程结束')
