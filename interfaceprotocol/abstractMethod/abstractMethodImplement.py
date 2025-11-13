"""
不同抽象基类的具体要求
"""
from collections.abc import MutableSequence, Mapping

"""
1. MutableSequence 的完整实现
"""

class FullyImplementedMutableList(MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial else []

    def __getitem__(self, index):
        print(f"获取索引 {index}")
        return self._items[index]

    def __setitem__(self, index, value):
        print(f"设置索引 {index} 为 {value}")
        self._items[index] = value

    def __delitem__(self, index):
        print(f"删除索引 {index}")
        del self._items[index]

    def __len__(self):
        return len(self._items)

    def insert(self, index, value):
        print(f"在索引 {index} 插入 {value}")
        self._items.insert(index, value)

    # 可以重写其他方法以获得更好性能
    def append(self, value):
        print(f"追加 {value}")
        self.insert(len(self), value)

    def reverse(self):
        print("反转列表")
        self._items.reverse()


# 测试所有功能
lst = FullyImplementedMutableList([1, 2, 3])
lst.append(4)  # 追加 4
lst[1] = 20  # 设置索引 1 为 20
del lst[0]  # 删除索引 0
lst.reverse()  # 反转列表
print(list(lst))  # [4, 3, 20]


"""
2. Mapping抽象基类的实现
"""

class SimpleDict(Mapping):

    def __init__(self, **kwargs):
        self._data = kwargs

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    # 自动获得 keys(), values(), items(), get() 等方法

simple_dict = SimpleDict(a=1, b=2, c=3)
print(simple_dict['a'])
print(list(simple_dict.keys()))
print(SimpleDict.__mro__)

