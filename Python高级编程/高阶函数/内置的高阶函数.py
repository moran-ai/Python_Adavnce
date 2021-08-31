"""
内置的高阶函数：
    map()函数：把可迭代对对象中的每一个元素转成一个的对象，并返回一个迭代器
    reduce函数：把可迭代对象中的每一个元素做聚合处理，返回一个聚合的值
    filter函数:把一个可迭代对象中的元素做过滤操作，如果func为True则留下，否则则过滤掉,返回一个迭代器
    max和min
    sorted 把一个可迭代对象里面的每个元素进行排序，返回一个列表
"""
lis = [1, 2, 34, 5, 6, 7]
it1 = map(lambda x: x ** 2, lis)
# print(next(it1))
# print(next(it1))
# print(list(it1))

from functools import reduce

my_list = [1, 23, 4, 5, 6, 6, 7, 8]
print(reduce(lambda x, y: x + y, my_list))


def getMax(x, y):
    if x > y:
        return x
    else:
        return y


print(reduce(getMax, my_list))

students = [
    {'name': 'k', 'age': 34},
    {'name': 'j', 'age': 23},
    {'name': 'jk', 'age': 18},
    {'name': 'jh', 'age': 90}
]
print(list(filter(lambda x: x['age'] > 18, students)))
print(max(students, key=lambda x: x['age']))
print(min(students, key=lambda x: x['age']))
print(sorted(students, key=lambda x: x['age'], reverse=True))
