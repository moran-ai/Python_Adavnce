"""
偏函数：在函数调用之前，就可以得知某些参数的值，这样函数有一个参数或者多个参数时，一部分参数可以预先知道，
这样函数就能以最少的参数进行调用，节约编程成本
"""
import functools

int_2 = functools.partial(int, base=2)  # base 代表进制

int_3 = functools.partial(int, base=2)


# print(int_3('1'))

# args形式的参数
def addCount(x, y):
    return x + y


add = functools.partial(addCount, 4)
# print(add(4))

# kwargs形式的参数
def show(name, age):
    return f'{name}--->{age}'


s = functools.partial(show, age=19)
# print(s('s'))

# 回调函数形式
def test(callback, name, age):
    callback(name, age)


c = functools.partial(show, age=23)


# print(c('z'))

# 解决回调函数参数的未知的情况
def show1(name, age):
    print(f'{name}--->{age}')


def ca(callback):
    print('回调函数参数未知执行')
    callback()


show_1 = functools.partial(show1, name='2', age=22)
ca(show_1)
