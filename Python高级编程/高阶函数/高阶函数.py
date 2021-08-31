# 定义一个函数，计算阶乘
def test1(num):
    if num == 1:
        return 1
    else:
        return num * test1(num - 1)

# test2是高阶函数   参数是有一个是函数
def tests2(list1, func):
    new_list = []
    for i in list1:
        new_list.append(func(i))
    return new_list


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tests2(list1, test1))
