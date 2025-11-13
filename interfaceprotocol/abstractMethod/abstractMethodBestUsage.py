"""
子类抽象化基类最佳实践
"""
from collections.abc import Sequence, MutableMapping

"""
1. 明确设计意图
"""

# 好的设计: 明确声明接口
class EmployeeList(Sequence):
    """明确表示这是一个只读的员工列表"""
    pass

# 不好的设计： 直接使用列表
class EmployeeList(list):
    """可能被误用，因为列表是可变的"""
    pass


"""
2. 提供有用的错误信息
"""

class BoundedList(MutableMapping):
    def __init__(self,max_size):
        self.max_size = max_size
        self._items = []

    def _check_bounds(self):
        if len(self._items) >= self.max_size:
            raise OverflowError(f"列表已满，最大容量: {self.max_size}")

    def insert(self,index,value):
        self._check_bounds()
        self._items.insert(index, value)

    def append(self,value):
        self._check_bounds()
        self._items.append(value)

    # 其他必须方法...