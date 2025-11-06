"""
静态方法的应用
"""
import math


class MathUtils:

    # 静态方法：与类相关但不依赖类或实例状态的工具函数
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def multipy(a,b):
        return a*b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * radius ** 2
# 使用静态方法
print(MathUtils.add(5,3))

print(MathUtils.is_even(5))

print(MathUtils.calculate_circle_area(2))

# 不需要创建实例即可使用
result = MathUtils.multipy(2,3)
print(result)
