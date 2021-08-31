import timeit


# 计算列表方法的时间复杂度
def list_append():
    lst = []
    for i in range(10001):
        lst.append(i)


def list_insert_head():
    lst = []
    for i in range(10001, -1, -1):
        lst.insert(0, i)


def list_insert_tail():
    lst = []
    for i in range(10001):
        lst.insert(-1, i)


def list_extend():
    lst = []
    for i in range(10001):
        lst.extend([i])


def list_concat_1():
    lst = []
    for i in range(10001):
        lst = lst + [i]


def list_concat_2():
    lst = []
    for i in range(10001):
        lst += [i]


def list_com():
    lst = [i for i in range(10001)]


def list_range():
    lst = list(range(10001))


func_list = [list_append, list_insert_head, list_insert_tail, list_extend, list_concat_1, list_concat_2,
             list_com, list_range]

for func in func_list:
    t = timeit.Timer('func()', globals={'func': func})
    # ljust对打印格式进行填充
    print(f'{func.__name__}运行时间：'.ljust(30), t.timeit(1000), '秒')
