def produce(c):
    print("--3、启动生成器，开始执行生成器consumer--")
    c.send(None)  # 3、启动生成器，开始执行生成器consumer
    print("--6、继续往下执行--")
    n = 0
    while n < 5:
        n += 1
        print("[Producer]: producing {} ..".format(n))
        print("--7、第{}次唤醒生成器，从yield位置继续往下执行！--".format(n + 1))
        r = c.send(n)  # 第二次唤醒生成器
        print('r的值是*******************************************************', r)
        print("--9、从第8步往下--")
        print("[Producer]: consumer return {} ..".format(r))

    c.close()


def consumer():
    print('--4、开始执行生成器代码--')
    response = None
    while True:
        print('--5、yield，中断，保存上下文--')
        n = yield response  # 4、yield，中断，保存上下文
        print('--8、获取上下文，继续往下执行--')
        if not n:
            return
        print("[Consumer]: consuming {} ..".format(n))
        response = "ok"


#
# if __name__ == "__main__":
#     c = consumer()  # 1、定义生成器，consumer并不执行
#     produce(c)  # 2、运行produce函数


# def pro(c):
#     print('启动生成器')
#     c.send(None)
#     n = 0
#     while n < 5:
#         n += 1
#         print(f'第{n}次唤醒生成器')
#         r = c.send(n)
#         print('r的值是', r)
#     c.close()
#
#
# def cum():
#     print('开始执行生成器代码')
#     response = None
#     while True:
#         c = yield response
#         print('c的值', c)
#         if not c:
#             return
#
#         response = 'ok'

# if __name__ == '__main__':
#     c = cum()
#     pro(c)


# def m():
#     a, b = 0, 1
#     response = None
#     while True:
#         a, b = b, a + b
#         a = yield response
#         print(a)
#         response = 'ok'

# def mm():
#     a, b = 0, 1
#     response = 0
#     while True:
#         c = yield response
#         print(c)
#         a, b = b, a + b
#         # response = response + a


# m = mm()
# print(m.__next__())
# print(m.__next__())


def m(s):
    print('启动生成器')
    s.send(None)
    n = 0
    while n < 5:
        n += 1
        print(f'第{n}次启动生成器')
        r = s.send(n)
        print(r)
    s.close()


def n():
    print('开启生成器')
    response = None
    while True:
        print('中断保存上下文')
        c = yield response
        print(c)
        print('继续执行')
        response = 'ok'
