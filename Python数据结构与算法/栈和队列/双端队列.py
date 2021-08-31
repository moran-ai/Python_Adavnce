# 双端队列 顺序表实现
class Dueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def length(self):
        return len(self.items)

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def push_left(self, item):
        return self.items.insert(0, item)

    def pop_right(self):
        return self.items.pop()

if __name__ == "__main__":
    dueue = Dueue()
    dueue.push(1)
    dueue.push(2)
    dueue.push_left(24)
    dueue.push_left(25)
    dueue.pop()
    dueue.pop_right()
    print(dueue.items)