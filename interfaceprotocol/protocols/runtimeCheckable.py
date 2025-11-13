"""
运行时可检查的静态协议
"""
from typing import Protocol, runtime_checkable


@runtime_checkable
class Readable(Protocol):
    def read(self) -> str:
        ...

class FileReader:
    def read(self) -> str:
        return "File content"

class StringReader:
    def read(self) -> str:
        return "String content"

def process_reader(reader: Readable) -> str:
    if isinstance(reader, Readable):  # 运行时可检查
        return reader.read()
    raise TypeError("Reader must implement read method")

file_reader = FileReader()
string_reader = StringReader()

print(process_reader(file_reader))
print(process_reader(string_reader))


"""
运行时协议检查的局限性
"""


@runtime_checkable # 13.6.2 启用运行时检查
class CanQuack(Protocol):
    def quack(self) -> str:
        ...

# --- 以下类 *没有* 继承 CanQuack ---
class Duck:
    def quack(self) -> str:
        return "Quack!"

class Person:
    def quack(self) -> str:
        return "I'm quacking like a duck!"

class Dog:
    def bark(self) -> str:
        return "Woof!"

# 13.6.1 在函数中使用协议
def make_it_quack(obj: CanQuack):
    print(obj.quack())

# --- 静态检查 (Mypy) ---
# mypy会检查 make_it_quack 的调用
make_it_quack(Duck())
make_it_quack(Person())
# make_it_quack(Dog()) # Mypy: Error! "Dog" has no attribute "quack"


# --- 运行时检查 (Python) ---
print(isinstance(Duck(), CanQuack))   # True (方法名匹配)
print(isinstance(Person(), CanQuack)) # True (方法名匹配)
print(isinstance(Dog(), CanQuack))    # False (没有quack方法)


class BadDuck:
    def quack(self, times: int) -> None: # 签名完全不同！
        print(f"Quack {times} times")

# 13.6.3 局限性体现！
print(isinstance(BadDuck(), CanQuack)) # True! (运行时只检查了 'quack' 方法是否存在)

# --- 静态检查 (Mypy) ---
# Mypy 仍然能发现 BadDuck 的问题
make_it_quack(BadDuck()) # Mypy: Error! 签名不兼容 TypeError: BadDuck.quack() missing 1 required positional argument: 'times'