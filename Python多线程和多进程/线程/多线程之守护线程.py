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
    thread_t = MyThreading(name='my_thread_1')
    thread_t.setDaemon(True)
    # thread_t.daemon = True 设置守护线程  主线程结束，子线程也结束
    thread_t.start()
    time.sleep(1)
    print('主线程结束')
