"""
参数化泛型与TypeVar
"""
from typing import TypeVar, Sequence, List, Tuple

# 定义类型变量
T = TypeVar('T')
U = TypeVar('U')

# 泛型函数
#    这个函数接受一个 T 类型的序列，并返回一个 T 类型的元素
def first_element(seq: Sequence[T]) -> T:
    return seq[0]

def zip_sequences(a: Sequence[T], b: Sequence[U]) -> List[Tuple[T, U]]:
    return list(zip(a, b))

# 受限类型变量
Number = TypeVar('Number', int, float)

def add_numbers(a: Number, b: Number) -> Number:
    return a + b

# 使用示例
first = first_element([1, 2, 3])
pairs = zip_sequences([1, 2, 3], ['a', 'b', 'c'])
result = add_numbers(5, 3.14)
print(first)
print(pairs)
print(result)