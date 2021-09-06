"""
@Author:hu
@Time:2021/9/4 13:09 
@File:类的方式创建上下文.py
@Software: PyCharm
"""
"""
通过类的方式创建上下文，需要定义__enter__和__exit__方法
"""


class Sample:
    def __enter__(self) -> object:
        """
        定义enter,用来表示进入资源之前的操作和处理
        :return:
        """
        print('enter resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        定义exit，用来表示资源结束之后或出现异常的处理逻辑
        :param exc_type: 异常的类型
        :param exc_val: 异常的输出值
        :param exc_tb: 异常抛出的运行堆栈
        :return:
        """
        print('exit')

    def doSomething(self) -> object:
        a = 1 / 1
        return a


def getSample() -> object:
    return Sample()


if __name__ == '__main__':
    with getSample() as sample:
        print('do something')
        sample.doSomething()
