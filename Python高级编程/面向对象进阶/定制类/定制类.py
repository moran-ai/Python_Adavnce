class Person:
    def __init__(self, name):
        self.name = name
        self.a = 0
        self.b = 1

    # 定制对象的描述信息
    def __str__(self):
        return f'Person object------>{self.name}'

    # 将对象变为一个可迭代对象，返回一个迭代器
    def __iter__(self):
        return self

    # 将对象变为一个迭代器
    def __next__(self):
        # 打印斐波拉契数列
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:  # 如果超出1000，则抛出异常
            raise StopIteration
        return self.a

    # 将对象当作list对待
    def __getitem__(self, item):  # item可能是一个下标，也可能是一个切片
        # 如果是下标
        if isinstance(item, int):
            a, b = 1, 1
            for i in range(item):
                a, b = b, a + b
            return a
        # 如果是切片
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0  # 给定初始值
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    # 访问对象中不存在的属性或者方法时，会出现错误AttributeError，如果不想看见这个错误，可以重写__getattr__方法
    def __getattr__(self, item):
        if item == 'age':
            return 19
        if item == 'eat':
            return lambda: print('eat函数执行')

    # 将对象变为一个函数
    def __call__(self, *args, **kwargs):
        print('person函数执行')


p = Person('jk')
print(p)
for i in p:
    print(i)

print('索引为5的值是：', p[5])
print('切片为5-10的值是：', p[5:10])
print('--------------------------------')
print(p.age)
p.eat()
p()
print(callable(p))  # 判断对象是否可以调用
