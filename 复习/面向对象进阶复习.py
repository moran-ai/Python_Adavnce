import types


class Person:
    __slots__ = ('name', 'age')


class Student:
    pass


"""
默认情况每一个类都会有一个dict,这个dict用来维护实例的所有属性,dict只保持实例的变量，不会保存类的属性
每次实例化都要分配一个dict，造成空间的浪费，因此有了__slots__,__slots__是一个元组，包括了当前的访问对象，
类的实例中只能使用__slots__中定义的属性，不能增加其他属性
注意：
    有了__slots__,类就不再有__dict__
"""
p = Person()
p.name = 'k'
p.age = 23
# print(p.age, p.name)
# print(p.__dict__)
# print(p.__hash__())
# print(p.__dir__())
# print(p.__module__)
s = Student()
s.name = '李梅'  # 给实例对象增加一个属性
Student.sex = '女'  # 给类添加一个属性


# 给实例对象添加一个方法
def func(self):
    return '这是实例对象的方法'


# 类添加一个静态方法
@staticmethod
def fun():
    return '给类添加一个静态方法'


Student.staticRun = fun


# 给类添加一个类方法
@classmethod
def f(cls):
    return '给类添加一个类方法'


Student.method = f
s.method = types.MethodType(func, s)
print(s.name, Student.sex, s.method(), Student.staticRun(), Student.method())
