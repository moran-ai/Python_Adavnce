"""
闭包：在函数中定义了一个内部函数，内部函数可以引用外部函数的变量，并且可以在函数定义之外被调用
闭包的三个条件：
    ① 必须有一个内部函数
    ② 内部函数必须定义在一个外部函数的闭合范围内，内部函数引用外部变量
    ③ 外部函数必须返回定义的内部函数
"""


def func_a(num_a):
    def func_b(num_b):
        print(f'内部函数func_b的参数是{num_b}, 外部函数func_a的参数是{num_a}')
        return num_a + num_b

    return func_b


# f = func_a(100)
# print(f(200))

# 闭包的应用
def create_line(a, b):
    def line(x):
        return a * x + b

    return line


l1 = create_line(2, 4)
l2 = create_line(9, -8)


# print(l1(4))
# print(l2(4))

def test1():
    c = 0  # c不是全局变量，是介于全局变量和局部变量之间的变量 需要使用nonlocal进行标识

    def add_test():
        nonlocal c
        # print(c)
        c += 1
        # print(c)
        return c

    return add_test


t = test1()()


# 闭包的陷阱
"""
这里给内部函数tes_添加了一个形参_i
如果不给内部函数添加形参,那么在内部函数执行之前，for循环里面的变量就已经发生了变化,for循环已经全部执行了一遍,这个变量会影响到
所有引用它的内部函数；在外部函数还没有返回内部函数之前，内部函数还不是闭包函数，只是一个普通的函数。
正确的做法应该是将父函数的局部变量赋值给闭包函数的形参。因为在函数在进行定义时，对形参的赋值会保存在当前函数的定义中，不会对
其他函数有影响
注意：
    如果内部函数没有返回外部函数的局部变量，就不是闭包
"""
def tes():
    add_list = []
    for i in range(1, 4):
        def tes_(_i=i):
            return _i ** 2

        add_list.append(tes_)
    return add_list


f1, f2, f3 = tes()
print(f1(), f2(), f3())
