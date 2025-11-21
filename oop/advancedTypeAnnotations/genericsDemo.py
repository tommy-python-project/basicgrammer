"""
泛型与泛化类
"""
from typing import TypeVar, Generic, List, Optional, Tuple

T = TypeVar('T')
U = TypeVar('U')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self) -> Optional[T]:
        if self._items:
            return self._items[-1]
        return None

    def is_empty(self) -> bool:
        return len(self._items) == 0


# 使用示例
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
value: int = int_stack.pop()

str_stack: Stack[str] = Stack()
str_stack.push("hello")

"""
多重类型参数的泛型
"""
K = TypeVar('K')
V = TypeVar('V')

class Pair(Generic[K, V]):
    def __init__(self, key: K, value: V) :
        self.key = key
        self.value = value

    def get_pair(self) -> Tuple[K, V]:
        return (self.key, self.value)

    def __repr__(self) -> str:
        return f"Pair({self.key}, {self.value})"

# 使用示例
pair1: Pair[int, str] = Pair(1, "one")
pair2: Pair[str, List[int]] = Pair("numbers", [1, 2, 3])