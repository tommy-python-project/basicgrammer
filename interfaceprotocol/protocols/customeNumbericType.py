"""
自定义数字类型
"""
from numbers import Rational
import math

from interfaceprotocol.protocols.numbericProtocol import check_number_hierarchy


class MyFraction(Rational):
    """自定义分数实现"""

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("分母不能为零")

        # 简化分数
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        self._denominator = value

    # 必需实现的抽象方法
    def __add__(self, other):
        if isinstance(other, MyFraction):
            new_num = (self.numerator * other.denominator +
                       other.numerator * self.denominator)
            new_den = self.denominator * other.denominator
            return MyFraction(new_num, new_den)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, MyFraction):
            return MyFraction(self.numerator * other.numerator,
                              self.denominator * other.denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, MyFraction):
            return (self.numerator == other.numerator and
                    self.denominator == other.denominator)
        return NotImplemented

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"MyFraction({self.numerator}, {self.denominator})"


# 测试自定义分数
f1 = MyFraction(3, 4)
f2 = MyFraction(1, 2)

print(f"f1 = {f1}")
print(f"f2 = {f2}")
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 * f2 = {f1 * f2}")
print(f"float(f1) = {float(f1)}")

# 检查类型层次
check_number_hierarchy(f1, "自定义分数")