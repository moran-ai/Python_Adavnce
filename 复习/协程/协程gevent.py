import gevent
from gevent import pool, Greenlet


def task1(num):
    for i in range(num):
        print(gevent.getcurrent(), i)  # gevent.getcurrent() 获得当前正在执行的greenlet
        gevent.sleep(2)


# if __name__ == '__main__':
#     # 创建协程 通过spawn方法进行创建协程的实例
#     g1 = gevent.spawn(task1, 5)
#     g2 = gevent.spawn(task1, 5)
#     g3 = gevent.spawn(task1, 5)
#     g1.join()
#     g2.join()
#     g3.join()
#     g3.get()  # 获得协程返回值
#     # print(g3.dead())  # 判断协程是否死亡
#     print(g3.loop)  # 获取事件循环对象
#     print(g3.value)  # 获取返回的值
#
#     # 捕获异常
#     print(g3.exception)
#     print(g3.exc_info)  # 详细的错误信息
#     print(g3.link_value())  # 执行成功的回调函数
#     print(g3.link_exception())  # 执行失败后的回调函数


