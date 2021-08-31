# Iterable:可迭代对象 能够通过for循环来遍历里面的元素的对象
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器
# 使用isinstance()方法判断一个对象是否是迭代器
"""
可迭代对象（list，set，dict）可以重复迭代，只能使用for循环；迭代器只能迭代一次，可以通过next或for进行迭代。
可迭代对象不能使用next函数调用但是可以使用for调用，而迭代器可以使用next，也可以使用for进行调用。
他俩最大的区别就是，可迭代对象可以无限迭代，而迭代器只能迭代一次（是个数据流的形式！）。
判断迭代器 ： isinstance([], Iterator)。
判断可迭代对象：  isinstance([], Iterable)。
迭代器一定是可迭代对象,可迭代对象不一定是迭代器对象
可迭代对象：
    内置__iter__方法的对象，就是可迭代对象，该方法可以不依赖索引取值
迭代器:
    内置__next__方法和__iter__的对象，就是迭代器对象

for循环本质为迭代器的循环
    原理：
        ① 调用in后面可迭代对象的__iter__方法，将可迭代对象变为迭代器
        ② 调用迭代器里面的__next__方法，将得到的返回值赋值给变量名
        ③ 循环往复，直到迭代器抛出异常，for循环会自动捕获异常然后结束循环
迭代器优点：
    ① 提供了一种通用不依赖索引进行迭代取值的方式
    ② 同一时刻内存中只存在一个值，更节省内存
迭代器缺点：
    ① 取值没有索引灵活，不能指定某一个值，只能往后不能往前
    ② 不能预测迭代器的长度
"""
from collections.abc import Iterable
from collections.abc import Iterator

a = {}
b = (1,)
c = []


def tesdt1(args):
    if isinstance(args, Iterable):
        print('是可迭代对象')
    else:
        print('不是可迭代对象')


# tesdt1(1)
def tesdt2(args):
    if isinstance(args, Iterator):
        print('是迭代器对象')
    else:
        print('不是迭代器对象')


# tesdt2((x for x in range(32)))

# 使用iter()将list,dict,str变为迭代器
tesdt2(iter(a))
