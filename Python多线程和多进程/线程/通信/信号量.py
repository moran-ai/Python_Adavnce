import threading
import time

# 创建一个信号量
Semap_hore = threading.BoundedSemaphore(3)  # 一次允许3个线程运行


def run(num):
    Semap_hore.acquire()
    print(f'第{num}个num')
    time.sleep(1)
    Semap_hore.release()


if __name__ == '__main__':
    for i in range(100):
        t = threading.Thread(target=run, args=(i,))
        t.start()
