"""
虚拟子类的register实际应用
"""
from collections.abc import Sequence


class BinaryTree:

    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        """前序遍历"""
        yield self.value
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right

# 注册为Sequence的虚拟子类
Sequence.register(BinaryTree)


tree = BinaryTree(1,
                 BinaryTree(2,
                           BinaryTree(3),
                           BinaryTree(4)),
                 BinaryTree(5))

print(isinstance(tree, Sequence))
print(list(tree))