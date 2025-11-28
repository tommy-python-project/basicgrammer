"""
类型约束和边界
"""
from typing import TypeVar, Iterable


# 带约束的泛型
def constrained_generics():
    """带约束的泛型"""

    print("=== 带约束的泛型 ===")

    # 带约束的类型变量
    Comparable = TypeVar("Comparable",int,float,str)
    Number = TypeVar("Number",int,float)

    def max_value(items: Iterable[Comparable]) -> Comparable:
        """找最大值 - 只支持可比较类型"""
        max_val = None
        for item in items:
            if max_val is None or item > max_val:
                max_val = item
            return max_val

    def average(numbers: Iterable[Number]) -> float:
        """计算平均值 - 只支持数值类型"""
        total = 0.0
        count = 0
        for num in numbers:
            total += num
            count += 1
        return total / count if count else 0.0


    # 测试
    integers = [1, 5, 3, 9, 2]
    floats = [1.5, 2.7, 3.1]
    strings = ["apple", "zebra", "banana"]

    print(f"整数最大值: {max_value(integers)}")
    print(f"浮点数最大值: {max_value(floats)}")
    print(f"字符串最大值: {max_value(strings)}")
    print(f"整数平均值: {average(integers)}")
    print(f"浮点数平均值: {average(floats)}")

    # 这会引发类型错误（如果使用类型检查器）
    # print(f"字符串平均值: {average(strings)}")  # 类型错误

constrained_generics()