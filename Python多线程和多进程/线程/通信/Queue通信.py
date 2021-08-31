import threading
import time
import queue

# 创建一个队列
q = queue.Queue(maxsize=1000)  # 先进先出队列  设置队列中存放的数据为1000


# q = queue.LifoQueue() # 后进先出队列
# q = queue.PriorityQueue()  # 优先级队列

# 创建一个生产者线程
class Producter(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            # q.size() 获取队列中的数据的总数
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = f'生产{count}'
                    # 将数据放入队列
                    q.put(msg)
                    print(msg)
            time.sleep(2)


class Customer(threading.Thread):
    def run(self):
       global q
       while True:
           for i in range(100):
               msg = q.get()
               print(f'消费{msg}')
           time.sleep(3)

if __name__ == '__main__':
    t1 = Producter()
    t2 = Customer()
    t1.start()
    t2.start()
