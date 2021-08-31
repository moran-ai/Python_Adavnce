"""
闭包：在一个函数中定义了一个内部函数，然后这个函数可以使用外部的变量，可以在外部被调用
闭包的条件：
    ① 必须有一个内部函数
    ② 内部函数必须定义外部函数的闭合范围内, 内部函数引用外部变量
    ③ 外部函数返回内部函数

注意：
    介于内部函数和外部函数之间的变量不是全局变量，需要使用nonlocal关键字进行声明
"""
a = 1


def wai():
    b = 1

    def nei():
        nonlocal b
        b += 1
        print('内部函数执行', a)
        print('介于外部函数和内部函数之间的变量', b)

    return nei


# wai()()


def my_func(*args):
    func_list = []
    for i in range(3):
        def func():
            return i
        func_list.append(func)
    return func_list


f1, f2, f3 = my_func()
print(f1())
print(f2())
print(f3())
