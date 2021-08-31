# 使用顺序表实现

class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        # 栈中添加一个元素
        return self.__data.append(item)

    def pop(self):
        # 栈中弹出一个元素
        if self.is_empty():
            raise ValueError('栈为空')
        return self.__data.pop()

    def top(self):
        # 返回栈顶元素
        if self.is_empty():
            raise ValueError('栈为空')
        return self.__data[-1]

    def is_empty(self):
        # 判断栈是否为空
        return self.__data == []

    def size(self):
        # 返回栈元素的个数
        return len(self.__data)

# if __name__ == "__main__":
#     stack = Stack()
#     # print(stack.push(1))
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     stack.push(4)

#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())


class Node:
    def __init__(self, data, _next):
        self.data = data
        self.next = _next


class Stack1:
    def __init__(self):
        self.__top = None
        self._size = 0

    def push(self, item):
        # 栈中添加一个元素
        # 让self.top指向新的结点
        self.__top = Node(item, self.__top)
        self._size += 1

    def pop(self):
        # 栈中弹出一个元素
        if self.is_empty():
            raise ValueError('栈为空')
        value = self.__top.data
        self.__top = self.__top.next
        self._size -= 1
        return value

    def top(self):
        # 返回栈顶元素
        if self.is_empty():
            raise ValueError('栈为空')
        return self.__top.data

    def is_empty(self):
        # 判断栈是否为空
        return self._size == 0

    def size(self):
        # 返回栈元素的个数
        return len(self._size)


if __name__ == "__main__":
    stack = Stack1()
    # print(stack.push(1))
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
