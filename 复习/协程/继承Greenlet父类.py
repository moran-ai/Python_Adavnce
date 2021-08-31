import gevent
from gevent import Greenlet

"""
继承Greenlet父类来创建协程对象
"""


class MyGreenLet(Greenlet):
    """
    自定义的一个协程类

    重写_run()方法
    """

    def __init__(self, timeout, msg):
        Greenlet.__init__(self)
        self.timeout = timeout
        self.msg = msg

    def _run(self):
        """
        执行协程
        :return:
        """
        print(f'自定义协程{MyGreenLet.__name__}执行---->{self.msg}')
        gevent.sleep(1)
        print(f'自定义协程{MyGreenLet.__name__}结束')


class My_Gevent:
    def __init__(self, timeout=1):
        self.timeout = timeout

    def run(self):
        g1 = gevent.spawn(self.tasks, 1, 'a')
        g2 = gevent.spawn(self.tasks, 2, 'b')
        g3 = MyGreenLet(self.timeout, 'c')
        g3.start()

        g_list = ([g1, g2, g3])
        gevent.joinall(g_list)

    def tasks(self, pid, msg):
        print(f'当前协程为{pid}, --->{msg}')
        gevent.sleep(2)
        print(f'当前协程{pid}结束')



if __name__ == '__main__':
    m = My_Gevent()
    m.run()
