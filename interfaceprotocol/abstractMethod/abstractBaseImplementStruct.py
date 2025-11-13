"""
用抽象基类实现结构类型
"""
from abc import ABC, abstractmethod
from typing import Any


class SupportsAdd(ABC):

    @abstractmethod
    def __add__(self, other: Any) -> Any: ...


class CustomNumber:

    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value + other.value)
        return CustomNumber(self.value + other)

SupportsAdd.register(CustomNumber)

def add_objects(a,b):
    if isinstance(a, SupportsAdd) and isinstance(b, SupportsAdd):
        return a + b
    raise TypeError("Objects must support addition")

num1 = CustomNumber(5)
num2 = CustomNumber(3)
result = add_objects(num1, num2)
print(result.value)  # 8