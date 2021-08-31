# 列表生成式
# list1 = [x for x in range(1, 10)]
# print(list1)

# 创建一个生成器 方式一：列表生成式
# 生成器不会把内容保存到内存中
# 生成器是一个对象，里面保存了产生元素的算法，同时会记录游标的位置
"""
遍历生成器中的内容：
    ① 内置的函数next()函数  获取第一个值
    ② for循环遍历
    ③ 使用object对象中的__next__()方法
    ④ 使用send函数  生成器第一次调用时需要传递 send(None) 后面没有限制
"""
list1 = (x for x in range(1, 10))
# print(list1)
# print(next(list1))
# print(next(list1))
# print(list1.__next__())
# print(list1.__next__())
# print(list1.__next__())
# for i in list1:
#     print(i)

# 通过列表生成式创建一个生成器
# g = (x for x in range(1, 10) if x % 2 == 0)

"""
斐波拉契数列：
    从第三项开始，每一项都等于前两行的和
"""


# 通过函数创建生成器 yield
def test():
    a, b = 0, 1
    while True:
        # yield用于创建生成器，返回后面的变量给生成器
        yield b  # b是斐波拉契数中的一个元素
        # print(b)
        a, b = b, (a + b)


g = test()
print(g.send(None))
print(g.__next__())
# g.send(None)
print(g.send('abc'))
print(g.send(1))
print(g.send(5))
print(g.send(6))
print(g.send(9))
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.send(None))
# print(g.send('hello'))
# print(g.__next__())
# print(g.send('1'))
# print(g.send(''))
# print(g.send(''))
