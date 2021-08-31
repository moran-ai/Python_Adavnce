import types


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student:
    __slots__ = ('name', 'sex')


if __name__ == '__main__':
    p = Person('jk', 90)

    # 给实例对象添加一个属性
    p.sex = '女'
    # 给类添加一个属性
    Person.address = '背景'


    # 给实例对象添加一个函数
    def run(self, work):
        print(f'正在{work}')


    p.method = types.MethodType(run, p)


    # p.method('学习')

    # 给类添加一个函数
    @classmethod
    def run1(cls, wokr1):
        print(f'这是类里面的函数{wokr1}')


    Person.method = run1


    # Person.method('s')

    # 给类添加一个静态函数
    @staticmethod
    def run2(wokr):
        print(f'这是类中的静态方法{wokr}')


    Person.staticRun = run2
    Person.staticRun('3')

    s = Student()
    s.name = 'jk'
    s.sex = '女'
    # s.age=24
    print(s.name, s.sex)
