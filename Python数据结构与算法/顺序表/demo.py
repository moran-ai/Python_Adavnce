"""
Python列表的实现原理
"""
PY_SIZE_T_MAX = float('inf')  # Python最大的容量
obj_size = 1
allocated = 0  # 容量
size = 0         # 元素个数
items = []     # 数据区


class List:
    def list_resize(self, new_size):
        allocated = self.allocated  # 获取当前对象的列表容量
        # allocated >> 1 右移1位 ===> allocated // 2
        # 元素的个数小于当前列举表的容量，大于右移的元素,如果满足这个条件，则将新的元素大小赋值给初始的大小
        if allocated >= new_size >= (allocated >> 1):
            # 将新的元素大小赋值给初始的元素大小
            self.size = new_size
            return 0
        # 如果不满足if的条件，则需要进行扩容
        # 新的容量等于新的元素大小加上新的元素右移的个数加上
        # 3 if new_size < 9 else 6 如果新的大小小于9则为3，否则为6
        new_allocated = new_size + (new_size >> 3) + (3 if new_size < 9 else 6)
        # 如果新的容量大小大于Python最大的容量，则返回-1
        if new_allocated > PY_SIZE_T_MAX:
            return -1

        # 如果新的元素个数为0，则代表新的容量为0
        if new_size == 0:
            new_allocated = 0

        # 计算容量需要的字节数
        num_allocated_bytes = new_allocated * obj_size
        # 获取到新的内存空间的地址
        items = addr(self.items, num_allocated_bytes)
        # 如果数据区为None，则返回-1
        if items == None:
            return -1
        # 让列表对象的数据区指向新的内存空间地址
        self.items = items
        self.allocated = new_size
        self.size = new_size
