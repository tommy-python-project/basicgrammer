"""
抽象基类的虚拟子类
"""
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        ...

# 注册为虚拟子类
class Dog:
    def speak(self):
        return "Woof!"

Animal.register(Dog) # 将Dog注册为Animal的虚拟子类
print(issubclass(Dog, Animal))
print(isinstance(Dog(), Animal))