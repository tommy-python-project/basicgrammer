"""
树状结构定义
"""
from collections import deque
from typing import Generic, TypeVar, List, Optional, Iterator, Callable


def tree_structure_demo():
    """树状结构遍历演示"""

    print("=== 遍历树状结构 ===")

    T = TypeVar('T')

    class TreeNode(Generic[T]):
        """通用树节点"""

        def __init__(self, value: T, children: Optional[List['TreeNode[T]']] = None):
            self.value = value
            self.children = children or []

        def __repr__(self) -> str:
            return f"TreeNode({self.value})"

    def traverse_tree(node: TreeNode[T]) -> Iterator[T]:
        """深度优先遍历树"""
        yield node.value
        for child in node.children:
            yield from traverse_tree(child)

    def traverse_tree_bfs(node: TreeNode[T]) -> Iterator[T]:
        """广度优先遍历树"""
        from collections import deque
        queue = deque([node])

        while queue:
            current = queue.popleft()
            yield current.value
            queue.extend(current.children)

    # 创建测试树
    root = TreeNode('A', [
        TreeNode('B', [
            TreeNode('D'),
            TreeNode('E')
        ]),
        TreeNode('C', [
            TreeNode('F', [
                TreeNode('G')
            ])
        ])
    ])

    print("深度优先遍历:")
    dfs_result = list(traverse_tree(root))
    print(f"  {dfs_result}")

    print("广度优先遍历:")
    bfs_result = list(traverse_tree_bfs(root))
    print(f"  {bfs_result}")


tree_structure_demo()

# 泛化树遍历器
def generic_tree_traverser():
    """泛化树遍历器"""

    print("\n=== 泛化树遍历器 ===")

    T = TypeVar('T')

    class TreeTraverser(Generic[T]):
        """通用的树遍历器"""
        def __init__(self,get_children_func: Callable[[T],Iterator[T]]):
            self.get_children = get_children_func

        def dfs(self,root:T) -> Iterator[T]:
            """深度优先遍历"""
            yield root
            for child in self.get_children(root):
                yield from self.dfs(child)

        def bfs(self,root:T) -> Iterator[T]:
            """广度优先遍历"""
            queue = deque([root])

            while queue:
                current = queue.popleft()
                yield current
                queue.extend(self.get_children(current))

    # 使用示例： 文件系统树
    class FileNode:
        def __init__(self, name: str,is_dir: bool = False,children = None):
            self.name = name
            self.is_dir = is_dir
            self.children = children or []


        def __repr__(self) -> str:
            return f"FileNode({self.name})"


    # 创建文件系统树
    file_tree = FileNode("root", True, [
        FileNode("documents", True, [
            FileNode("file1.txt"),
            FileNode("file2.txt")
        ]),
        FileNode("pictures", True, [
            FileNode("photo1.jpg"),
            FileNode("photo2.jpg")
        ]),
        FileNode("readme.txt")
    ])

    # 创建遍历器
    traverser = TreeTraverser[FileNode](lambda node: node.children)

    print("文件系统深度优先遍历:")
    for node in traverser.dfs(file_tree):
        print(f"  {node.name}")

generic_tree_traverser()
