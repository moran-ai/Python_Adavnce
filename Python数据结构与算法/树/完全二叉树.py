class Node:
    def __init__(self, val):
        self.val = val  # 数据域
        self.left = None  # 左指针域
        self.right = None  # 右指针域


class Tree:
    def __init__(self):
        self.root = None  # 树的根节点

    def add(self, val):
        """
        广度优先遍历
        :param val:  要添加节点的值
        :return:
        """
        # 往树中添加一个节点，并保证这棵树仍然是完全二叉树
        node = Node(val)
        # 判断树是否为空，如果为空，直接将node设置为根节点
        if not self.root:
            self.root = node
            return
        # 从上往下，从左往右遍历整颗树，然后找到第一个空位
        # 把节点添加进去
        # 创建一个列表，用来存储每一层的节点
        queue = [self.root]
        while True:
            cur_node = queue.pop(0)
            # 判断左边是否有空位，如果有空位，就添加对应的元素
            if not cur_node.left:
                cur_node.left = node
                return
                # 判断右边是否有空位，如果有空位，就添加对应的元素
            elif not cur_node.right:
                cur_node.right = node
                return
            # 如果都没有空位，就将左右两个节点添加到要判断的节点列表中去
            queue.extend((cur_node.left, cur_node.right))

    def show(self):
        """
        展示树
        :return:
        """
        if not self.root:
            return
        # 从上往下，从左往右遍历整颗树，然后找到第一个空位
        # 把节点添加进去
        # 创建一个列表，用来存储每一层的节点
        queue = [self.root]
        i = 1
        while queue:
            size = len(queue)
            print(f'第{i}层', end='\t')
            for _ in range(size):
                node = queue.pop(0)
                print(node.val, end=' ')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
            i += 1

    def preorder(self):
        # 先序遍历
        def helper(root):
            if not root:
                return
            print(root.val, end=' ')  # 输出根节点
            helper(root.left)  # 左子树
            helper(root.right)  # 右子树

        helper(self.root)
        print()

    def inoder(self):
        # 中序遍历
        def helper(root):
            if not root:
                return
            helper(root.left)
            print(root.val, end=' ')
            helper(root.right)

        helper(self.root)
        print()

    def postorder(self):
        # 后序遍历
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            print(root.val, end=' ')

        helper(self.root)
        print()


def buildTree(preorder, inoder):
    """
    根据先序遍历结果和中序遍历结果构建二叉树
    :param preorder:  先序遍历
    :param inoder:    中序遍历
    :return:
    """
    # 递归结束条件
    if not preorder:
        return
    # 在中序遍历中找到根节点的索引
    in_indx = inoder.index(preorder[0])
    # 构建根节点
    node = Node(preorder[0])
    # 构建左子树
    node.left = buildTree(preorder[1: in_indx + 1], inoder[:in_indx])
    # 构建右子树
    node.right = buildTree(preorder[in_indx + 1:], inoder[in_indx + 1:])
    return node


if __name__ == '__main__':
    tree = Tree()
    tree.root = buildTree(
        [0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 6],
        [7, 3, 8, 1, 9, 4, 10, 0, 5, 2, 6]
    )
    tree.show()