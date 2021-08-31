# 队列实现 链表
class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class Queue:
    def __init__(self, size):
        self.head = None  # 队列头部
        self.rear = None  # 队列尾部
        self._length = 0  # 队列长度
        self.size = size  # 队列最大长度

    def is_empty(self):
        return self._length == 0

    def length(self):
        return self._length

    def push(self, item):
        if self.length() == self.size:
            raise ValueError('队列已满')
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self._length += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('队列为空')
        value = self.head.data
        self.head = self.head.next
        self._length -= 1
        return value

    def peek(self):
        if self.is_empty():
            return ValueError('队列为空')
        return self.head.data


if __name__ == "__main__":
    q = Queue(4)
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.length())
    print(q.peek())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
