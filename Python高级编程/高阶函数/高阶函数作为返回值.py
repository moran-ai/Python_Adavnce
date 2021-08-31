def get_num(*args):
    def t():
        s = 0
        for i in args:
            s += i
        return s

    return t


f = get_num(1, 23, 4, 5, 6, 8, 90)


# print(f())

# 定义一个函数，来打印出100以内的所有质数 0和1不是质数，2是最小的质数
def get_num():
    """
    获取所有的奇数
    :return:
    """
    n = 1
    while True:
        n += 2
        yield n


f = get_num()


# 定义一个函数，用来过滤奇数中不是质数
def my_filter(n):
    return lambda x: x % n > 0


# 定义一个质数生成器
def t():
    yield 2
    # 拿到所有的奇数
    g = get_num()
    while True:
        # 从生成器中拿取奇数
        x = next(g)
        # 过滤掉不是质数的奇数
        g = filter(my_filter(x), g)
        yield x


for i in t():
    if i < 100:
        print(i)
    else:
        break
