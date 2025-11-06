"""
算术运算符
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """加法: v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """减法: v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """乘法: v * scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """除法: v / scalar"""
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self):
        """取负: -v"""
        return Vector(-self.x, -self.y)

    def __abs__(self):
        """绝对值: abs(v)"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# 使用示例
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)  # Vector(4, 6)
print(v1 * 2)  # Vector(6, 8)
print(abs(v1))  # 5.0