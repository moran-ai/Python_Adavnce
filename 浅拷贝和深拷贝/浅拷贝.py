"""
@Author:hu
@Time:2021/9/6 13:37 
@File:浅拷贝.py
@Software: PyCharm
"""
import copy

# # a = [1, 2, 3, 4, 5, [9, 0]]
# # b = copy.copy(a)
# # print('外层元素id')
# # print(id(a))
# # print(id(b))
# # #
# # # print(a)
# # # print(b)
# # a[5][0] = 10
# # # print(a)
# # # print(b)
# # print('内部元素的id')
# # print(id(a[1]))
# # print(id(b[1]))
#
# a = [1, 23, 3, 4, 5, 6]
# b = copy.copy(a)
# print(id(a))
# print(id(b))
#
# print(a)
# print(b)
#
# # b[6][0] = 10
# b[1] = 10
# print(id(a))
# print(id(b))
# print(id(a[1]))
# print(id(b[1]))
# print(a)
# print(b)

l1 = [1, 2, 3]
l2 = l1
l1[0]=11
print(l1)
print(l2)
