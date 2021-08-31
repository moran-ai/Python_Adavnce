import sys

lst = []
# 初始容量  64
init_allocate = sys.getsizeof(lst)  # 返回一个对象占用的内存，以字节为单位

# 向列表中添加元素
for i in range(1, 100):
    lst.append(i)
    now_allocate = sys.getsizeof(lst) - init_allocate
    # 一个整数是4个字节，1个字节是8位，一个整数就是32位
    print(f'当前元素的数量:{i}, 当前的占用内存:{now_allocate}字节,当前的容量是：{now_allocate // 8}')
