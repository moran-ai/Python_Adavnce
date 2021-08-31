class UppattrMetaclass(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for name, value in attrs.items():
            if not name.startswith('__'):
                new_attrs[name.upper()] = value
        return type.__new__(cls, name, bases, new_attrs)


class Person(object, metaclass=UppattrMetaclass):
    name = 'jk'
    age = 'jk'


print(hasattr(Person, 'name'))
print(hasattr(Person, 'NAME'))


