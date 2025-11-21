"""
泛型静态协议
"""
from abc import abstractmethod
from typing import TypeVar, Protocol, Any

T = TypeVar('T')

class SupportsAdd(Protocol):
    """支持加法操作的协议"""

    @abstractmethod
    def __add__(self: T, other: T) -> T: ...

class SupportsCompare(Protocol):
    """支持比较操作的协议"""

    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

    @abstractmethod
    def __eq__(self, other: Any) -> bool: ...

# 使用协议约束泛型函数
def add_values(a: T, b: T) -> T:
    """只能用于支持加法的类型"""
    return a + b

# 自定义类实现协议
class Vector:
    def __init__(self,x: float,y: float) :
        self.x = x
        self.y = y

    def __add__(self,other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


# 使用示例
v1 = Vector(1,2)
v2 = Vector(3,4)
result = add_values(v1,v2)
print(result)  # Vector(4, 6)