"""
迭代器：
   内置了 __iter__和__next__

可迭代对象:
   内置了 __iter__
判断一个对象是否是可迭代对象或者迭代器
isinstance()
将一个可迭代对象变为迭代器
    iter() 或者 __iter__()

迭代器一定是可迭代对象，可迭代对象不一定能是迭代器
"""
from collections.abc import Iterable, Iterator

d = iter('aaa')


# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d1)
# print(isinstance(d, Iterator))

class Person:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    # def __new__(cls, *args, **kwargs):
    #     pass


# p = Person()
# print(issubclass(p))
# print(p)
# print(isinstance(p, Iterable))
# print(isinstance(p, Iterator))

# 生成器

