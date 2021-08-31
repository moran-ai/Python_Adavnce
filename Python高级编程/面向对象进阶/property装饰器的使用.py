class Student:
    def get_age(self):
        return self._age

    def set_age(self, value):
        if value >= 0 and value <= 88:
            self._age = value
        else:
            raise ValueError('年龄必须在0到88之间')


class Student1:
    @property
    def age(self):
        return self._age

    @age.setter  # 当前属性值可以修改
    def age(self, value):
        if value >= 0 and value <= 88:
            self._age = value
        else:
            raise ValueError('年龄必须在0到88之间')

    @property  # 对外暴露的是name，实际上的属性值应该是self._name
    def name(self):
        self._name = '张三'
        return self._name


if __name__ == '__main__':
    s = Student1()
    s.age = 23
    # s.name = 'i'
    print(s.age)  # age可读可写
    print(s.name)  # name只可读
