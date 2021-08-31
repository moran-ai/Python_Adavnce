# 创建元类的方式
"""
元类：用来创建类的类
1.通过导包语句
from ... import  ... 这个时候  python解释器自动调用type函数创建了一个元类
2.手动通过type函数
type(类名, 父类, 属性)
自定义元类:
    ① 通过继承type，自定义元类
    class Class_xxx(type):
        里面可以使用__new__方法用来创建一个新的对象，但是进行返回时，需要返回type.__new__(cls, name, bases, attrs)
            cls:这个类本身
            name:名字
            bases:父类
            attrs:属性
        def __new__(cls, name, bases, attrs):
            ...
            return type.__new__(cls, name, bases, attrs)
    ② 通过def的方式
    不使用__new__方法，在返回时使用type(name, bases, attrs)函数进行创建
    def xxx(name, bases, attrs):
        name:名字
        bases:父类
        attrs:属性
        return type(name, bases, attrs)
hasattr(obj, attr)  查看对象是否有指定的属性 返回值为boolean
3.__class__ 查看对象的类型
4.__metaclass__ 用来创建类
如果当前类中有metaclass属性，那么就会使用当前这个类当中的metaclass属性进行类的创建
如果当前类中没有metaclass属性，那么就会使用在父类当中寻找metaclass属性
如果父类中没有metaclass属性，就会使用type进行类的创建
5.元类设置静态方法[@staticmethod]和类方法[@classmethod]
@classemethod
def class_method():
    print('class_method')

@staticmethod
def static_method():
    print('static_method')
type(name, bases, {'attr': attr, 'static_method': static_method, 'class_method': 'class_method'}


类方法：需要和类进行交互，不需要和实例进行交互。类方法和实例方法相似，但传递的不是类的实例，而是类本身。可以通过类实例或者类本身调用
静态方法：和类相关，和类的实例和属性无关 可以通过类的实例对象或者类本身进行调用
"""


def sa(name):
    print(f'{name}')


# Person = type('Person', (object,), {'sa': sa})

class Me(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for name, value in attrs.items():
            if not name.endswith('__'):
                new_attrs[name.upper()] = value
        return type.__new__(cls, name, bases, attrs)


class P(metaclass=Me):
    Name = 'kjk'
    name = 'k'


# print(hasattr(P, 'name'))

class C:
    a_attr = 'a'

    @staticmethod
    def s():
        print('静态方法执行')

    @classmethod
    def a(cls):
        print('类方法执行')
        print(cls.a_attr)
        print(cls.b)

    def b(self):
        print('实例方法执行')


c = C()
# c.b()
c.a()
# c.s()
