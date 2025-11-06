"""
属性描述符的替代
"""

class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def _validate_positive_number(self, value, name):
        """验证正数"""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{name}必须是正数")
        return value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = self._validate_positive_number(value, "宽度")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = self._validate_positive_number(value, "高度")

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

# 使用示例
rect = Rectangle(5,3)
print(f"面积：{rect.area}")
print(f"周长：{rect.perimeter}")

try:
    rect.width = -5  # 会抛出 ValueError
except ValueError as e:
    print(f"错误: {e}")

