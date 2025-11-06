"""
静态协议
"""
from typing import Protocol


# 1. 定义一个协议，说明你需要什么方法
class HashName(Protocol):
    def get_name(self) -> str:
       ... # 方法体不重要

# 2. 定义一个使用该协议的函数
def greet_object(obj: HashName) :
    print(f"Hello {obj.get_name()}")

# 3. 定义*任何*实现了该协议的类（注意：不需要继承HasName）
class Person:
    def get_name(self) -> str:
        return "Alice"

class Building:
    def get_name(self) -> str:
        return "Empire State"

# 使用
print(greet_object(Person()))
print(greet_object(Building()))



