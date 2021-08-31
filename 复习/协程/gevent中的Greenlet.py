# # import gevent
# import time
# from greenlet import greenlet
#
# """
# greenlet使用switch来切换协程
# """
#
#
# def test1(g, gr):
#     for i in range(100):
#         print('------- 协程A ---------')
#         g.switch(gr, g)  # 手动切换协程
#         time.sleep(1)
#
#
# def test2(g, gr):
#     s = 'afdjasfjsajdfasoifiiififififififiiaisiiifah'
#     for i in s:
#         print('------- 协程B ---------')
#         g.switch(gr, g)  # 手动切换协程
#         time.sleep(1)
#
#
# #
# # if __name__ == '__main__':
# #     g1 = greenlet(test1)
# #     g2 = greenlet(test2)
# #     g1.switch(g2, g1)  # 手动进行协程的切换
#
#
# def test3():
#     for _ in range(100):
#         print('------ 协程A ------')
#         # gr.switch(g, gr)
#         gevent.sleep(1)
#
#
# def test4():
#     for _ in range(100):
#         print('------ 协程B ------')
#         # gr.switch(g, gr)
#         gevent.sleep(1)
#
#
# def test5():
#     for _ in range(100):
#         print('------ 协程C ------')
#         # gr.switch(g, gr)
#         gevent.sleep(1)
#
#
# # if __name__ == '__main__':
# #     # g1 = greenlet(test3)
# # g2 = greenlet(test4)
# # g3 = greenlet(test5)
# # # g1.switch(g2, g1)
# # g2.switch(g3, g2)
# # # g1.switch(g2, g3)
# # g1 = gevent.spawn(test3)
# # g2 = gevent.spawn(test4)
# # g3 = gevent.spawn(test5)
# # gevent.joinall([g1, g2, g3])
#
# import gevent
# import signal
#
#
# def func_fover():
#     gevent.sleep(1000)
#
#
# # import gevent
# # from gevent import Timeout
# #
# # seconds = 3
# # timeout = Timeout(seconds)
# # timeout.start()
# #
# #
# # def wait():
# #     gevent.sleep(4)
# #
# #
# # try:
# #     gevent.spawn(wait).join()
# # except Timeout:
# #     print('Could not complete')
import time
#
#
def echo(i):
    time.sleep(0.001)
    return i
#
#
# # Non Deterministic Process Pool
from multiprocessing.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, range(10))]
run2 = [a for a in p.imap_unordered(echo, range(10))]
run3 = [a for a in p.imap_unordered(echo, range(10))]
run4 = [a for a in p.imap_unordered(echo, range(10))]
print(run1 == run2 == run3 == run4)
# Deterministic Gevent Pool
from gevent.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, range(10))]
run2 = [a for a in p.imap_unordered(echo, range(10))]
run3 = [a for a in p.imap_unordered(echo, range(10))]
run4 = [a for a in p.imap_unordered(echo, range(10))]
print(run1 == run2 == run3 == run4)
