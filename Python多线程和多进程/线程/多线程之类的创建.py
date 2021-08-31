import threading
import time, os


class MyThreading(threading.Thread):
    def run(self):
        for i in range(3):
            print(f'线程名字{self.name},输出:{i}')
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print(f'主线程开始时间{start}')
    s = 'abcdef'
    thread_list = []
    for i in range(5):
        thread_t = MyThreading(name=s[i])
        thread_t.start()
        thread_list.append(thread_t)

    for j in thread_list:
        j.join()
    end = time.time()
    print(f'主线程结束，时间为{(end - start):.2f}')
