"""
支持静态协议
"""
from typing import TypeVar, Protocol, Iterable

T = TypeVar('T')

class SupportsLessThan(Protocol):
    def __lt__(self : T, other: T) -> bool: ...

def max_item(items: Iterable[SupportsLessThan]) -> SupportsLessThan:
    return max(items)

# 支持任何实现了__lt__的类型
print(max_item([3, 1, 4,1,5]))
print(max_item(['a', 'b', 'c']))