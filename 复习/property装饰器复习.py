"""
装饰器property作用：
    ① 用来修饰方法，将方法变为一个属性
    ② 与定义的属性结合使用，防止属性被修改
"""


class Student:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0 and value <= 88:
            self._age = value
        else:
            raise ValueError('错误')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


# s = Student()
# s.age = 1
# s.name = '李梅'
# print(s.age, s.name)

class M:
    def get_m(self):
        return self._m

    def set_m(self, value):
        if value >= 0 and value <= 88:
            self._m = value
            # print(value)
        else:
            raise ValueError('值错误')

    v = property(get_m, set_m)


m = M()
m.v = 4
print(m.v)
