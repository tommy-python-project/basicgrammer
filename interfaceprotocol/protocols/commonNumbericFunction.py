"""
number模块中的抽象基类与Numeric协议

通用数学函数
"""
import math
from decimal import Decimal
from fractions import Fraction
from numbers import Real


def safe_sqrt(x: Real) -> float:
    """
    安全的平方根计算，接受任何实数类型
    使用 numbers.Real 进行类型检查
    """
    if not isinstance(x, Real):
        raise TypeError(f"期望实数类型，得到 {type(x).__name__}")

    if x < 0:
        raise ValueError("不能对负数求平方根")

    return math.sqrt(x)

# 测试通用函数
def test_safe_sqrt():
    """测试通用平方根函数"""
    test_cases = [
        25,
        2.25,
        Fraction(9,4),
        Decimal('6.25')
    ]
    for case in test_cases:
        try:
            result = safe_sqrt(case)
            print(f"sqrt({case}) = {result} (类型: {type(result).__name__})")
        except (ValueError, TypeError) as e:
            print(f"sqrt({case}) 错误: {e}")

test_safe_sqrt()