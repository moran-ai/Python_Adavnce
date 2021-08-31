import sys


class TestObject:
    def __init__(self):
        # hex 十六进制
        print(f'当前对象已被创建，当前对象的地址是{hex(id(self))}')


# a = TestObject()
# print(f'当前对象的引用计数为{sys.getrefcount(a)}')
# b = a
# c = a
# print(f'当前对象的引用计数为{sys.getrefcount(a)}')
"""
dir不带参数时，返回当前范围内的变量，方法和定义的类型列表
dir带参数时，返回参数的属性，方法列表
"""

# print(dir(TestObject))
import types


class P:
    pass


def eat(self):
    print('吃法')


@staticmethod
def r():
    print('pao')


e = P()
# e.eat = eat
# e.eat()
e.method = types.MethodType(eat, e)
e.method()

P.staticRun = r
P.staticRun()
