import gevent


def ask(name):
    print(f'{name}: 买mac笔记本')
    gevent.sleep(2)  # 人为模拟IO阻塞
    print(f'{name}: 买macpro')


def answer(name):
    print(f'{name}: 买')
    gevent.sleep(2)  # 人为模拟IO阻塞
    print(f'{name}: maimai')


if __name__ == '__main__':
    # 创建一个协程
    g = gevent.spawn(ask, 'kkk')
    g1 = gevent.spawn(answer, '哈哈')
    gevent.joinall([g, g1])  # 自动切换并执行
