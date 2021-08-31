import time
from greenlet import greenlet


def g1():
    while True:
        print('this is a g1')
        g2.switch()
        time.sleep(1)


def g2():
    while True:
        print('this is a g2')
        g1.switch()
        time.sleep(1)


if __name__ == '__main__':
    g1 = greenlet(g1)
    g2 = greenlet(g2)
    g1.switch()

def g3(name):
    while True:
        print(f'this is {name}')
        g4.switch('b')
        time.sleep(1)


def g4(name):
    while True:
        print(f'this is {name}')
        g3.switch()
        time.sleep(1)


if __name__ == '__main__':
    g3 = greenlet(g3)
    g4 = greenlet(g4)
    g3.switch('a')
