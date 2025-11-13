"""
numeric 静态协议

定义numeric协议
"""
from typing import TypeVar, runtime_checkable, Protocol, List

T = TypeVar('T')

@runtime_checkable
class Numeric(Protocol):
    """数值类型协议，定义基本的数值操作"""

    def __add__(self: T, other: T) -> T: ...

    def __sub__(self: T, other: T) -> T: ...

    def __mul__(self: T, other: T) -> T: ...

    def __truediv__(self: T, other: T) -> T: ...

    def __abs__(self) -> T: ...

    def __neg__(self) -> T: ...

    def __pos__(self) -> T: ...


@runtime_checkable
class ComparableNumeric(Numeric,Protocol):
    """可比较的数值协议"""
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...


"""
2- 使用Numberic协议的通用函数
"""

N = TypeVar('N',bound = Numeric)


def normalize_data(data: List[N]) -> List[N]:
    """数据归一化：将数据缩放到 [0, 1] 范围"""

    if not data:
        return []

    if not all(isinstance(x,ComparableNumeric) for x in data):
        raise TypeError("所有元素必须支持比较操作")

    min_val = min(data)
    max_val = max(data)

    if min_val == max_val:
        return [x - min_val for x in data]  # 全部归零

    return [(x - min_val) / (max_val - min_val) for x in data]


def dot_product(a: List[N], b: List[N]) -> N:
    """点积计算，支持任何数值类型"""
    if len(a) != len(b):
        raise ValueError("向量长度必须相同")

    if not a:
        raise ValueError("向量不能为空")

    return sum(x * y for x, y in zip(a, b))

# 测试通用数值函数
def test_numeric_functions():
    """测试通用数值函数"""

    # 整数测试
    int_data = [1, 2, 3,4,5]
    print(f"整数归一化: {normalize_data(int_data)}")

    # 浮点数测试
    float_data = [1.0, 2.5, 3.7, 4.2, 5.8]
    print(f"浮点数归一化: {normalize_data(float_data)}")

    # 点积测试
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    print(f"整数点积: {dot_product(vec1, vec2)}")

    vec1_float = [1.5, 2.5, 3.5]
    vec2_float = [0.5, 1.5, 2.5]
    print(f"浮点数点积: {dot_product(vec1_float, vec2_float)}")

test_numeric_functions()




