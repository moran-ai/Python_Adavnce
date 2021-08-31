import gevent
from gevent import Greenlet

"""
使用继承Greenlet方式生成协程实例，不会将任务自动加入调度队列，需要使用start方法手动加入
"""


class MyGevent(Greenlet):
    def __init__(self, timeout, msg):
        Greenlet.__init__(self)
        self.timeout = timeout
        self.msg = msg

    def _run(self):
        print(f'继承Greenlet{self.msg}')
        gevent.sleep(self.timeout)
        print(f'继承Greenlet结束')


class TestGevent:
    def __init__(self, timeout=1):
        self.timeout = timeout

    def run(self):
        # 创建协程实例
        g0 = gevent.spawn(self.tasks, 1, 'work')
        g1 = Greenlet.spawn(self.tasks, 2, 'run')
        g3 = MyGevent(self.timeout, 'eat')
        g3.start()  # 手动将协程任务加入调度队列

        gevent.joinall([g0, g1, g3])  # 将协程任务添加到事件循环
        print('tasks done')

    def tasks(self, pid, msg):
        """
        协程任务函数
        :param pid: 协程id
        :param msg: 协程信息
        :return:
        """
        print(f'this is task{pid}, want to{msg}')
        gevent.sleep(1)
        print(f'this task{pid}done')


if __name__ == '__main__':
    t = TestGevent()
    t.run()
