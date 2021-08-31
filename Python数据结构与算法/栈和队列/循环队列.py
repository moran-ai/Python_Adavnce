# 循环队列 使用顺序表实现
class Queue:
    def __init__(self, size):
        self.items = [None] * size  # 规定数据区的大小
        self.head = 0  # 队首的索引
        self._length = 0  # 队列的长度
        self.size = size   # 队列的大小

    def is_empty(self):
        return self._length == 0

    def length(self):
        return self._length

    def push(self, item):
        if self.length() == self.size:
            raise ValueError('队列已满')
        # 计算要添加元素的索引
        idx = (self.head + self.length()) % self.size
        self.items[idx] = item
        self._length += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('队列为空')
        value = self.items[self.head]
        self.head = (self.head+1) % self.size
        self._length -= 1
        return value

    def peek(self):
        if self.is_empty():
            return ValueError('队列为空')
        return self.items[self.head]


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
