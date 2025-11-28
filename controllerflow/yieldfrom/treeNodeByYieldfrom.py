"""
yield from 遍历树状结构
"""

class TreeNode:
    def __init__(self, value,children=None):
        self.value = value
        self.children = children or []

    def __repr__(self):
        return f'TreeNode({self.value})'


def traverse_tree(node):
    yield node.value
    for child in node.children:
        yield from traverse_tree(child)

# 创建树结构
root = TreeNode('A',[
    TreeNode('B',[
        TreeNode('D'),
        TreeNode('E')
    ]),
    TreeNode('C',[
        TreeNode('F')
    ])
])

print(list(traverse_tree(root)))