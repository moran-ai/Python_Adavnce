class Father:
    def work(self):
        print('父亲的工作')


class Mather:
    def work(self):
        print('母亲的工作')


class Children(Father, Mather):  # 有多个父类，多个父类有相同的方法，按照优先级进行调用
    def __init__(self, name):
        self.name = name

    def work(self):
        print('自己的工作')


c = Children('jk')
c.work()
print(Children.__mro__)  # 打印Children的继承结构，按照优先级
