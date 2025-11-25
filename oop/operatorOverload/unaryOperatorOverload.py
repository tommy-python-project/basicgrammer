"""
一元运算符重载
"""
import math


class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    # 字符串表示
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # --- 一元运算符 ---
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


    def __neg__(self):
        """取反"""
        return Vector(-self.x, -self.y)

    def __pos__(self):
        """取正：+v （通常返回自身）"""
        return Vector(self.x, self.y)

    # 算术运算符
    def __add__(self,other):
        """重载加法运算符 v1 + v2"""
        if isinstance(other,Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """重载减法运算符 v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self,other):
        """重载乘法运算符 v * scalar 或 scalar * v"""
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self,other):
        """重载右乘法运算符 scalar * v"""
        return self.__mul__(other)

    def __truediv__(self,other):
        """重载除法运算符 v / scalar"""
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented

    # 比较运算符
    def __eq__(self,other):
        """重载等于运算符 =="""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self,other):
        """重载不等于运算符 ！="""
        return not self.__eq__(other)

    def __lt__(self,other):
        """重载小于等于运算符 <="""
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented

    def __gt__(self,other):
        """重载大于运算符 >"""
        if isinstance(other, Vector):
            return abs(self) > abs(other)
        return NotImplemented

    def __ge__(self,other):
        if isinstance(other, Vector):
            return abs(self) >= abs(other)
        return NotImplemented

    # 增量赋值运算符重载
    def __iadd__(self,other):
        """重载增量加法运算符 +="""
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        return NotImplemented

    def __isub__(self,other):
        """重载增量减法运算符 -="""
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            return self
        return NotImplemented

    def __imul__(self,other):
        """重载增量减法运算符 *="""
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            return self
        return NotImplemented

    # 矩阵乘法 @
    def __matmul__(self,other):
        """重载 @ 运算符作为点积运算"""
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __rmatmul__(self,other):
        """右点积运算"""
        return self.__matmul__(other)

# 测试 @ 运算符
v1 = Vector(2, 3)
v2 = Vector(4, 5)

dot_product = v1 @ v2
print(f"v1 @ v2 = {dot_product}")  # 2*4 + 3*5 = 23




# 测试基本运算符
v1 = Vector(2, 3)
v2 = Vector(1, 1)

print("v1 =", v1)  # Vector(2, 3)
print("v2 =", v2)  # Vector(1, 1)
print("-v1 =", -v1)  # Vector(-2, -3)
print("v1 + v2 =", v1 + v2)  # Vector(3, 4)
print("v1 - v2 =", v1 - v2)  # Vector(1, 2)
print("v1 * 3 =", v1 * 3)  # Vector(6, 9)
print("3 * v1 =", 3 * v1)  # Vector(6, 9)
print("v1 / 2 =", v1 / 2)  # Vector(1.0, 1.5)
print("abs(v1) =", abs(v1))  # 3.605551275463989


# 测试比较运算符
v3 = Vector(1, 1)  # 长度 ≈ 1.414
v4 = Vector(3, 4)  # 长度 = 5
v5 = Vector(1, 1)

print(f"v3 == v4: {v3 == v4}")  # False
print(f"v3 == v5: {v3 == v5}")  # True
print(f"v3 != v4: {v3 != v4}")  # True
print(f"v3 < v4: {v3 < v4}")    # True
print(f"v3 > v4: {v3 > v4}")    # False
print(f"v3 <= v5: {v3 <= v5}")  # True


# 测试增量赋值运算符
print("====测试增量赋值运算符====")
# 测试增量赋值运算符
v1 = Vector(2, 3)
v2 = Vector(1, 1)

print("初始 v1 =", v1)
v1 += v2
print("v1 += v2 后 =", v1)  # Vector(3, 4)

v1 *= 2
print("v1 *= 2 后 =", v1)  # Vector(6, 8)

v1 -= Vector(1, 2)
print("v1 -= Vector(1, 2) 后 =", v1)  # Vector(5, 6)