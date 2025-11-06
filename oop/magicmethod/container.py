"""
容器类型的魔术方法
"""

class MyContainer:

    def __init__(self):
        self.items = []

    def __len__(self):
        """返回长度：len(obj)"""
        return len(self.items)

    def __getitem__(self, key):
        """获取元素：obj[key]"""
        return self.items[key]

    def __setitem__(self, key, value):
        """设置元素：obj[key] = value"""
        self.items[key] = value

    def __delitem__(self, key):
        """删除元素：del obj[key]"""
        del self.items[key]

    def __contains__(self, key):
        """包含检查：key in obj"""
        return key in self.items

    def __iter__(self):
        """返回迭代器 for item in obj"""
        return iter(self.items)

    def __reversed__(self):
        """反向迭代，reversed(obj)"""
        return reversed(self.items)

# 使用示例
container = MyContainer()
container.items = [1, 2, 3,4]
print(len(container))
print(container[2])
container[2] = 10
print(3 in container)
for item in container:
    print(item,end=" ")
