def odd_num():
    n = 1
    while True:
        n += 2
        yield n


g1 = odd_num()


def my_filter(n):
    return lambda x: x % n > 0


def tt():
    yield 2
    g = odd_num()
    while True:
        y = next(g)
        g = filter(my_filter(y), g)
        # g = filter(lambda x :x % y > 0 ,g)
        yield y


for i in tt():
    print(i)
    if i > 100:
        break
