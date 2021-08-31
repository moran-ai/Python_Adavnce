# 双端队列，链表实现
class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class Dueue:
    def __init__(self):
        self.head = None  # 队头
        self.rear = None  # 队尾
        self._length = 0  # 队列长度

    def is_empty(self):
        return self._length == 0

    def length(self):
        return self._length

    def push(self, item):
        # 在队尾添加一个元素
        node = Node(item)
        # 队列为空
        if self.is_empty():
            self.head = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self._length += 1

    def push_left(self, item):
        # 在队首添加一个元素
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.rear = node
        else:
            node.next = self.head
            self.head = node
        self._length += 1

    def pop(self):
        # 弹出队首元素
        if self.is_empty():
            raise ValueError('双端队列为空')
        value = self.head.data
        self.head = self.head.next
        self._length -= 1
        if self._length == 0:
            self.rear.next = None
        return value

    def pop_right(self):
        # 弹出队尾的元素
        if self.is_empty():
            return ValueError('双端队列为空')
        cur = self.head  # 从队首开始进行遍历
        value = self.rear.data
        while cur.next != self.rear:
            cur = cur.next  # 找到尾结点
        self.rear = cur  # 尾部指针指向要删除元素的前一个元素
        cur.next = None  # 前一个元素的指针域改为None
        self._length -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError('双端队列为空')
        return self.head.data

    def items(self):
        cur = self.head
        while cur:
            print(cur.data, ' ', end=' -> ')
            cur = cur.next
        print()
    
if __name__ == "__main__":
    dueue = Dueue()
    dueue.push(1)
    dueue.push(2)
    dueue.push_left(24)
    dueue.push_left(25)
    dueue.items()
    dueue.pop()
    dueue.items()
    dueue.pop_right()
    dueue.items()