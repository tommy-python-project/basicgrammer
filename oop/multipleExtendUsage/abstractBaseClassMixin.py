"""
抽象基类也是混合类
"""
from abc import ABC, abstractmethod


class Drawable(ABC):
    """可绘制对象的抽象基类"""

    @abstractmethod
    def draw(self):
        pass

    def get_bounds(self):
        """提供默认实现"""
        return (0,0,100,100)

class Movable(ABC):
    """可移动对象的抽象基类"""

    @abstractmethod
    def move(self,x,y):
        pass

    def get_position(self):
        return (0,0)

class Resizable(ABC):
    """可调整大小对象的抽象基类"""

    @abstractmethod
    def resize(self,width,height):
        pass


# 具体类继承多个抽象
class Rectangle(Drawable,Movable,Resizable):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing rectangle at ({self.x}, {self.x})")

    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"Rectangle moved to ({x}, {y})")

    def resize(self, width, height):
        self.width = width
        self.height = height
        print(f"Rectangle resized to {width}x{height}")

    def get_bounds(self):
        return (self.x, self.y, self.width, self.height)

    def get_position(self):
        return (self.x, self.y)


# 使用
rect = Rectangle(10, 20, 100, 50)
rect.draw()
rect.move(30, 40)
rect.resize(150, 75)
print(f"Bounds: {rect.get_bounds()}")
