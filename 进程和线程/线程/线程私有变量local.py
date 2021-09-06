# @Author:hu
# @Time:2021/9/1 10:39 
# @File:线程私有变量local.py
# @Software: PyCharm
"""
线程私有变量local
多个线程访问全局变量，如果涉及到对全局变量的修改，操作，那么就会出现数据不同步的问题，
可以使用互斥锁来进行解决，也可以使用local【线程私有变量】
"""
import threading
import time

# 创建一个全局变量local  各个线程都可以进行访问
local = threading.local()


def process_thread(res):
    # print('--->', res)  # t1, t2
    # local.resource=t1 or local.resource=t2
    local.resource = res  # 在全局变量中定义一个变量resource 即为线程的局部变量 会将全局变量中属性进行拷贝到自己的存储空间
    process()  # 拷贝完成后，开始执行后面的函数


def process():
    # 获取当前线程关联的资源
    rep = local.resource  # 虽然名字相同，但是存储的是不同的线程
    print(local.resource)
    print('***>', rep)
    rep = rep + '111'
    print(rep)


# 定义2个线程
# t1 = threading.Thread(target=process_thread, args=('t1',))
# t2 = threading.Thread(target=process_thread, args=('t2',))
# t1.start()
# t2.start()


def work():
    local.x = 0
    for i in range(100):
        time.sleep(0.0001)
        local.x += 1
    print(threading.current_thread().getName(), local.x)


for i in range(5):
    thread = threading.Thread(target=work)
    thread.start()
    thread.join()
