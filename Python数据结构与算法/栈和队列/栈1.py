"""
遍历字符串：
    遇到左边括号，就入栈
    遇到右边括号，栈是否为空
    为空  ----> False
    不为空，弹出栈顶元素
    弹出的栈顶元素和遇到的右边括号进行匹配，看是否是相同类型
    不同类型，返回False
    相同类型,继续向下进行遍历
    如果字符串全部匹配完了，
    栈为空   -----> 返回True
    栈不为空  -----> 返回False
"""


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


def func(string):
    stack = Stack()
    dic = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for char in string:
        # 判断遇到的是左括号还是右括号
        if char in '([{':
            stack.push(dic[char])
        else:
            # 如果栈为空，或者栈中弹出的元素不匹配，返回False
            if stack.is_empty() or stack.pop() != char:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    print(func('[({})]'))
