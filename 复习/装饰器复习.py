# from functools import wraps
#
#
# # 定义一个装饰器
# def test(func):
#     @wraps(func)
#     def do():
#         print('开始')
#         func()  # 这个函数就是eat函数
#         print(func.__name__)  # eat
#         print('结束')
#
#     return do
#
#
# # @test
# def eat():
#     print('吃饭')
#
#
# a = test(eat)
# print(a.__name__)  # do这个函数
# a()

# import time
# from functools import wraps
#
#
# def logging(file_path='logging.log'):
#     def logg(func):
#         @wraps(func)
#         def lo(*args, **kwargs):
#             l = f'[info]--->时间为：{time.strftime("%H-%M-%S", time.localtime())}'
#             with open(file_path, 'a') as f:
#                 f.write(l)
#             return func(*args, **kwargs)
#
#         return lo
#
#     return logg
#
# @logging(file_path='lo.log')
# def work():
#     print('okk')
#
# @logging()
# def work1():
#     print('ok')
#
# work1()

import time
from functools import wraps

# def log(path='lo.log'):
#     def logging(func):
#         @wraps(func)
#         def lo(*args, **kwargs):
#             l = f'[info]---->时间为：{time.strftime("%H-%M-%S", time.localtime())}'
#             with open(path, 'a', encoding='utf-8') as f:
#                 f.write(l)
#             return func(*args, **kwargs)
#
#         return lo
#
#     return logging
#
#
# @log(path='ll.log')
# def work():
#     print('ok')

# work()

#
# def demo(x):
#     for i in reversed(range(0, x)):
#         print(' ' * (x - i) + "* " * (i + 1))


# demo(5)

# class Fn:
#     def __init__(self, path):
#         self.path = path
#
#     def __call__(self, func):
#         @wraps(func)
#         def lo(*args, **kwargs):
#             l = f'[info]--->{time.strftime("%H-%M-%S", time.localtime())}'
#             with open(self.path, 'a', encoding='utf-8') as f:
#                 f.write(l)
#             return func(*args, **kwargs)
#         return lo
#
# @Fn(path='l.log')
# def work():
#     pass
#
# work()

# import random
#
#
# def randon_num(num_max, number):
#     num_lst = []
#     while len(num_lst) < number:
#         num = random.randint(1, num_max)
#         if num in num_lst:
#             continue
#         else:
#             num_lst.append(num)
#     return num_lst
#
#
# if __name__ == '__main__':
#     print(len(randon_num(613, 120)))

import time
from functools import wraps


def t(loo='lo.log'):
    def lo(func):
        @wraps(func)
        def l(*args, **kwargs):
            t = f'[info]--->时间为：{time.localtime()}'
            with open(loo, 'a', encoding='utf-8') as f:
                f.write(t)
            func(*args, **kwargs)

        return l

    return lo


@t()
def wo():
    pass


# wo()

