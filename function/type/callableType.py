"""
callable
Callable 用于注解函数、lambda 表达式或任何可调用的对象。
"""
from typing import Callable


# 一个接受“函数” 作为参数的函数
# 这个 "函数" (fn) 必须接受两个 int，并返回一个 int
def apply_operation(a: int, b: int,fn: Callable[[int,int],int]) -> int:
    return fn(a, b)

def add(x: int, y: int) -> int:
    return x + y

def multiply(x: int, y: int) -> int:
    return x * y

result_add = apply_operation(5, 3, add)
result_mul = apply_operation(5, 3, multiply)
print(result_add)
print(result_mul)