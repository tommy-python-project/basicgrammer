"""
1. 基础层次结构演示
"""
from numbers import Number, Complex, Real, Rational, Integral


def check_number_hierarchy(obj,obj_name):
    """检查对象在数字层次结构中的位置"""
    print(f"\n=== 检查 {obj_name} ({type(obj).__name__}) ===)")
    print(f"是 Number:    {isinstance(obj, Number)}")
    print(f"是 Complex:   {isinstance(obj, Complex)}")
    print(f"是 Real:      {isinstance(obj, Real)}")
    print(f"是 Rational:  {isinstance(obj, Rational)}")
    print(f"是 Integral:  {isinstance(obj, Integral)}")


# 测试不同的数字类型
check_number_hierarchy(42,"整数 42")
check_number_hierarchy(3.14, "浮点数 3.14")
check_number_hierarchy(1 + 2j, "复数 1+2j")
check_number_hierarchy(22/7, "分数 22/7")
check_number_hierarchy(True, "布尔值 True")  # bool 是 int 的子类
check_number_hierarchy(10.0, "浮点数 10.0")
check_number_hierarchy(10, "整数 10")
