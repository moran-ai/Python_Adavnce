"""
装饰器的作用：给已经存在的函数添加额外的功能
"""
from functools import wraps


# 定义一个装饰器
# @wraps的作用：保留原函数，不让装饰器函数取代原函数
def test1(func):
    @wraps(func)  # 使用@wraps包装func
    def test2():
        print('ok')
        func()
        print('pl')

    return test2


@test1
def test3():
    print('hahah')


test3()
print(test3.__name__)  # test3
