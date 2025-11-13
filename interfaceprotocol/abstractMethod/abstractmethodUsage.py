"""
抽象方法实际应用场景
"""
from collections.abc import Set, MutableMapping

"""
1. 自定义集合类型
"""

class UniqueList(Set):
    """保持插入顺序的集合"""
    def __init__(self,iterable=()):
        self._items = []
        self._set = set()
        for item in iterable:
            self.add(item)

    def __contains__(self, value):
        return value in self._set

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def add(self, value):
        if value not in self._set:
            self._set.add(value)
            self._items.append(value)

    def __repr__(self):
        return f"UniqueList({self._items})"

unique = UniqueList([3, 1, 4, 1, 5, 9, 2, 6, 5])
print(unique)


"""
2. 带验证的字典
"""

class ValidatedDict(MutableMapping):

    def __init__(self,validator=None):
        self._data = {}
        self.validator = validator or (lambda k, v: True)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        if not self.validator(key, value):
            raise ValueError(f"无效的键值对: {key}={value}")
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)

# 使用验证器
def positive_number_validator(key, value):
    return isinstance(value, (int, float)) and value > 0

positive_dict = ValidatedDict(positive_number_validator)
positive_dict['age'] = 25      # 成功
try:
    positive_dict['score'] = -5  # 失败
except ValueError as e:
    print(f"错误: {e}")