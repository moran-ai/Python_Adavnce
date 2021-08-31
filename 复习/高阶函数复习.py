"""
内置的高阶函数
map:将可迭代对象中的每一个元素转换为一个新的对象，返回一个迭代器
reduce:对可迭代对象进行聚合处理 ,返回一个聚合的值
filter:对可迭代对象进行过滤处理，为True留下，False去掉
max and min
sorted:对可迭代对象进行排序，返回一个list
"""
from functools import reduce
from collections.abc import Iterator, Iterable


def map_func():
    lst = [1, 2, 3, 4, 5]
    lst_ = map(lambda x: x ** 2, lst)
    return lst_


def reduce_func():
    lst = [1, 2, 3, 4, 5, 5]
    lst_ = reduce(lambda x, y: x + y, lst)
    return lst_


def filter_func():
    lst = [1, 2, 3, 4, 5, 5]
    lst_ = list(filter(lambda x: x > 4, lst))
    return lst_


def max_fun():
    lst = [1, 2, 3, 4, 5, 5]
    lst_ = max(lst, key=lambda x: x)
    return lst_


def min_fun():
    lst = [1, 2, 3, 4, 5, 5]
    lst_ = min(lst, key=lambda x: x)
    return lst_


def sorted_func():
    lst = [1, 2, 0, 4, 5, 5]
    lst_ = sorted(lst, key=lambda x: x)
    return lst_


def return_func(*args, **kwargs):
    def f():
        for i in args:
            print(i)

    return f


lst = [1, 2, 0, 4, 5, 5]
l = return_func(lst)
l()
