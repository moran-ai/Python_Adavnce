import random


def cdx(f, he):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    c = random.randrange(1, 7)
    f = [a, b, c]
    he = a + b + c
    isbig = 11 <= he <= 18
    issmall = 3 <= he <= 10
    if isbig:
        return 'big'
    else:
        return 'small'
    xz = ['big', 'small']
    yourxz = input('请选择大小，big/small')
    if yourxz in xz:
        if yourxz == isbig:
            print('您赢了您的结果是', a, b, c)
        elif yourxz == ismall:
            print('您赢了您的结果是', a, b, c)
        else:
            print('您输了，您的结果是', a, b, c)


cdx('big', 34)
