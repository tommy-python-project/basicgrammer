"""
理解不同场景下使用继承的原因
继承应该在“is-a”关系时使用
"""
from abc import ABC, abstractmethod


# 正确的继承场景：明确的 is-a 关系
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        print("Sleeping...")


class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

# 混合类： 提供横切关注点
class LoggableMixin:
    def log(self,message):
        print(f"[LOG] {self.__class__.__name__}: {message}")

class SerializableMixin:
    def to_dict(self):
        return {key: value for key, value in self.__dict__.items()
                if not key.startswith('_')}


# 接口继承：定义契约
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Animal,Flyable,LoggableMixin,SerializableMixin):
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "Chirp!"

    def fly(self):
        self.log(f"{self.name} is flying")
        return "Flying high!"

# 使用
sparrow = Bird("Sparrow")
print(sparrow.speak())
print(sparrow.fly())
sparrow.log("Action completed")
print(sparrow.to_dict())