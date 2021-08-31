from greenlet import greenlet


# 创建一个协程案列，一问一答
def ask(name):
    print(f'{name}: 买mac笔记本')
    g1.switch('k')
    print(f'{name}: 买macpro')
    g1.switch()


def answer(name):
    print(f'{name}: 买')
    g.switch()
    print(f'{name}: maimai')

if __name__ == '__main__':
    # 创建一个协程
    g = greenlet(ask)
    g1 = greenlet(answer)
    g.switch('o')  # 函数第一次调用时需要传递参数
