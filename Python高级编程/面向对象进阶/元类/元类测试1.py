# 定义一个元类，用来将属性名全部转为大写
def upper_attr(class_name, class_bases, class_attrs):
    new_attrs = {}
    for name, value in class_attrs.items():
        if not name.startswith('__'): # 判断是否是私有属性
            new_attrs[name.upper()] = value
    return type(class_name, class_bases, new_attrs)


class Person(object, metaclass=upper_attr):
    name = 'jk'
    age = 23


print(hasattr(Person, 'name'))
print(hasattr(Person, 'NAME'))
print(hasattr(Person, 'AGE'))
