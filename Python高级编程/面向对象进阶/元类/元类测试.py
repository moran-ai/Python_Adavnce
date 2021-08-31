# 第一种方式
# from Python高级编程.面向对象进阶.元类.元类 import Person
# 引入模块之后，动态创建了一个Person类  本质上python解释器自动调用了type函数创建了一个类

# def say(name):
#     print(f'{name}在吃饭')


# # 第二种方式
# # 使用type()函数创建一个类  参数一：类名，参数二：父类 参数三：类中的方法或者属性
# Person = type('Person', (object,), dict(say=say))


# 第三种方式  使用metaClass创建一个元类
class PersonMetaClass(type):
    def __new__(cls, name, bases, attrs):
        """
        __new__ 创建一个实例
        :param name:  类的名字
        :param bases: 父类
        :param attrs: 属性
        """

        def func(cls, words='jk'):
            print(f'{words}吃啊哈哈')

        attrs['say'] = func
        return type.__new__(cls, name, bases, attrs)


# # 通过元类来创建一个类
class Person(object, metaclass=PersonMetaClass):
    def __init__(self):
        pass



p = Person()
p.a = 2
print(p.a)

# p.say('jk')
# print(type(p))
# print(type(Person))
# a = 1
# print(a.__class__.__class__)  # __class__指向该实例对应的类，然后可以调用该类对应的属性


