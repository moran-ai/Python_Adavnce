# 使用顺序表实现
class Queue:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return self.items == []

    def length(self):
        return len(self.items)

    def push(self, item):
        if self.length() == self.size:
            raise ValueError('队列已满')
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError('队列为空')
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return ValueError('队列为空')
        return self.items[0]


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
