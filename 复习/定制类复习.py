"""
python中的常用魔术方法
__str__:自定义对象的描述信息
__call__:将对象变为一个函数，可调用
__iter__: 将对象变为一个可迭代对象
__next__:将对象变为迭代器
__getitem__:将对象变为list
__getattr__:重写错误信息
__del__:销毁对象，解释器会自动进行调用
__hash__:返回hash值
__repr__:类似于__str__方法
__new__:实例化对象
__eq__:比较两个对象是否相同
__init__:初始话对象属性
"""
from collections.abc import Iterator, Iterable


class Person:
    def __init__(self):
        self.name = '李梅'
        self.a, self.b = 0, 1

    # 将对象变为可迭代对象
    def __iter__(self):
        return self

    # 将对象变为迭代器
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        """
        将对象变为list
        需要进行判断传递进来的item是index[索引]还是slice[切片]
        :param item:
        :return:
        """
        # 如果是index
        if isinstance(item, int):
            self.a, self.b = 1, 1
            for _ in range(item):
                self.a, self.b = self.b, self.a + self.b
            return self.a

        # 如果是slice
        elif isinstance(item, slice):
            # 获取传进来的start和stop
            start = item.start
            stop = item.stop
            # 如果start为None，需要进行判断
            if start is None:
                start = 0

            self.a, self.b = 1, 1
            l = []
            for _ in range(stop):
                if _ >= start:
                    l.append(self.a)
                self.a, self.b = self.b, self.a + self.b
            return l

    def __call__(self, *args, **kwargs):
        """
        将类变为一个函数，允许被调用
        :param args:
        :param kwargs:
        :return:
        """
        print('Person进行了调用')

    def __getattr__(self, item):
        """
        如果访问类中没有的属性，会出现AttributeError错误，需要进行相应的处理,不让出现提示
        :param item:
        :return:
        """
        if item == 'age':
            return 15
        elif item == 'eat':
            return lambda: print('ok')


p = Person()
print(isinstance(p, Iterator))
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print('索引为2的元素：', p[2])

print('切片为2到5的元素：', p[2:9])
p()
print(p.age)
p.eat()
# callable判断对象是否可以进行调用
print(callable(p))


