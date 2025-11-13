"""
子类化抽象基类
"""
from collections.abc import MutableSequence, Sequence


class CustomList(MutableSequence):

    def __init__(self, initial_data=None):
        self._data = list(initial_data) if initial_data else []

    # 必须实现抽象基类要求的抽象方法
    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def insert(self, index, value):
        self._data.insert(index, value)


class IncompleteSequence(Sequence):

    def __getitem__(self, index):
        return index

    # 缺少 __len__ 方法！
    # def __len__(self):
    #     return 10

# 尝试实例化会报错
try:
    obj = IncompleteSequence()
except TypeError as e:
    print(f"错误: {e}")  # TypeError: Can't instantiate abstract class IncompleteSequence wi


"""
方法实现依赖关系
Sequence 抽象基类的方法依赖
"""

class SmartSequence(Sequence):

    def __init__(self,data):
        self._data = data
    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    # 可选： 重写默认实现以获得更好性能
    def __contains__(self, value):
        print("使用优化的包含检查")
        return value in self._data

    def __index__(self, value):
        print("使用优化的索引查找")
        for i, item in enumerate(self.data):
            if item == value:
                return i
        raise ValueError


seq = SmartSequence([10, 20, 30, 20, 40])
print(20 in seq)        # 使用优化的包含检查 → True
print(seq.index(20))    # 使用优化的索引查找 → 1