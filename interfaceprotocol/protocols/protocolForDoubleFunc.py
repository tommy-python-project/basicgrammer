"""
为函数double添加类型提示
"""
from typing import TypeVar, Protocol

T = TypeVar('T',covariant=True)

class SupportsDouble(Protocol):

    def __mul__(self: T,other: int) -> T:
        ...

def double(x : SupportsDouble) -> SupportsDouble:
    return x * 2

# 支持任何实现了 __mul__ 的类型
print(double(5))
print(double(3.14))
print(double("hi"))