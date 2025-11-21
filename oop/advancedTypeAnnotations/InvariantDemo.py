"""
不变性
"""
from typing import TypeVar, Generic


class Animal:
    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):
    def speak(self) -> str:
        return "woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

T = TypeVar("T")

class MutableBox(Generic[T]):

    def __init__(self, value: T) -> None:
        self._value = value

    def get(self) -> T:
        return self._value

    def set(self,value: T) -> None:
        self._value = value

# 不变类型 - 严格的类型匹配
animal_box: MutableBox[Animal] = MutableBox(Animal())
dog_box: MutableBox[Dog] = MutableBox(Dog())

# 以下代码会导致类型错误：
animal_box = dog_box # 错误！
dog_box = animal_box # 错误！