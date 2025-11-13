"""
定义并使用一个抽象类
"""
import math
from abc import ABC, abstractmethod


# 定义一个抽象基类
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

# 尝试实例化ABC（失败）
# shape = Shape() # TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'area'

# 子类化ABC
class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius


    def area(self) -> float:
        # 必须实现 area 方法
        return math.pi * self.radius * self.radius


# 现在可以实例化子类
c = Circle(10)
print(c.area()) # 314.159...

# 检查也通过
print(isinstance(c, Shape)) # True
print(issubclass(Circle, Shape)) # True