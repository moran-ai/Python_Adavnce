class Node:
    # 结点类
    # 第一个结点的指针域为None
    def __init__(self, data, _next=None):
        self.data = data  # 数据域
        self._next = _next  # 指针域


class SingleLinkList:
    def __init__(self):
        self.head = None  # 链表的头,用来指向第一个结点
        self._length = 0  # 链表的长度

    def is_empty(self):
        # 判断链表是否为空
        return self._length == 0

    def length(self):
        # 获取链表的长度
        return self._length

    def nodes_list(self):
        # 返回链表中的所有的节点的值组成的列表
        res = []  # 返回一个列表
        cur = self.head  # 从链表头部进行搜索
        while cur:  # 链表如果不为空，则进行循环
            # 每循环一次，进链表的值存放到列表中
            res.append(cur.data)
            # 继续向下遍历
            cur = cur._next
        # 最终返回一个列表
        return res

    def add(self, data):
        # 链表的头部添加一个结点，值为data
        # 新建一个结点Node
        node = Node(data)
        # 让新的结点指向当前结点的头节点
        node._next = self.head
        # 再让链表的head指向当前结点
        self.head = node
        # 每增加一个结点，链表的长度加1
        self._length += 1

    def append(self, data):
        # 链表的尾部添加结点，值为data
        # 新建一个结点node
        node = Node(data)
        # 找到链表的尾结点
        # 从头开始，遍历链表中的所有结点
        # 每次判断结点的指针域是否为空
        # 如果为空则代表这是最后一个结点，然后让最后一个结点指向当前这个新的结点
        if self.head:  # 如果链表不为空  空值没有._next属性
            # 不为空则继续往下判断
            cur = self.head  # 从头部开始
            # 使用while循环判断结点的指针域是否为空
            while cur._next:
                cur = cur._next
            # 如果为空，当前结点的指针域指向新的结点
            cur._next = node
        else:
            self.head = node
        # 添加以后，链表的长度加1
        self._length += 1

    def insert(self, pos, data):
        # 指定位置添加结点 值为data
        # 插入两种情况
        # ① 插入的数据不对
        if pos <= 0:  # 插入的数据大于小于0，默认是第一个
            self.add(data=data)
        elif pos > self._length:  # 插入的数据大于链表的长度，默认是最后一个
            self.append(data=data)
        else:
            # 创建一个新的结点
            node = Node(data=data)
            # ② 正常情况  在pos-1和pos之间进行插入
            cur = self.head
            # 如果索引
            while pos-1:
                cur = cur._next  # cur为当前的pos-1的结点
                pos -= 1
            # 新的结点的指针域指向pos-1的结点的下一个结点
            node._next = cur._next
            # pos-1的结点指针域指向新的结点
            cur._next = node
            self._length += 1

    def remove(self, data):
        # 删除第一个值为data的结点
        cur = self.head  # 头节点
        prev = None  # 要删除结点的前驱结点
        while cur:
            if cur.data == data:
                # print(data)
                # 如果没有前驱结点，即为头结点
                if not prev:
                    self.head = cur._next
                # 有前驱结点，表示不是头节点
                else:
                    prev._next = cur._next
                self._length -= 1
                return 0
            prev = cur
            cur = cur._next
        return -1

    def modify(self, pos, data):
        if 0 <= pos < self._length:
            # 修改指定位置的元素值
            cur = self.head
            while pos:
                cur = cur._next
                pos -= 1
            cur.data = data
        else:
            raise IndexError

    def search(self, data):
        # 查找结点是否存在
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur._next
        return False


if __name__ == "__main__":
    n = SingleLinkList()
    print(n.head, n.length())
    n.add(1)
    print(n.head.data, n.length())
    n.add(2)
    print(n.head.data, n.length())
    n.add(4)
    print(n.head.data, n.length())
    print(n.nodes_list())
    n.append(5)
    print(n.head.data, n.length())
    print(n.nodes_list())
    n.append(6)
    print(n.nodes_list())
    n.add(8)
    print(n.nodes_list())
    n.insert(1, 10)
    print(n.nodes_list())
    n.insert(2, -1)
    print(n.nodes_list())
    n.insert(-2, -9)
    print(n.nodes_list())
    n.remove(-9)
    print(n.nodes_list())
    # n.modify(9, 9)
    print(n.nodes_list())
    print(n.search(3))
    print(n.search(5))