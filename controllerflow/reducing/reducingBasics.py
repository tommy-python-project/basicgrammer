"""
functools.reduce - 通用规约函数
基本用法
"""
import functools


def reduce_basics():
    """reduce函数基础"""
    print("\n=== functools.reduce 基础 ===")

    numbers = [1,2,3,4,5]

    # 手动实现求和
    def add(a,b):
        return a+b

    result = functools.reduce(add, numbers)
    print(f"reduce(add,{numbers}) = {result}")

    # 使用lamdba表达式
    result_lambda = functools.reduce(lambda a,b: a+b, numbers)
    print(f"reduce(lambda a,b: a+b, {numbers}) = {result_lambda}")

    # 提供初始值
    result_with_initial = functools.reduce(add, numbers,10)
    print(f"reduce(add, {numbers}, 10) = {result_with_initial}")

reduce_basics()


"""
reduce 工作原理
"""
def reduce_mechanics():
    """reduce函数工作原理"""
    print("\n=== reduce 工作原理 ===")

    def traced_add(a,b):
        print(f"  add({a}, {b}) = {a + b}")
        return a + b

    numbers = [1,2,3,4]
    print(f"计算 reduce(add, {numbers}):")
    result = functools.reduce(traced_add, numbers)
    print(f"最终结果: {result}")

    print(f"\n计算 reduce(add,{numbers},10):")
    result_with_initial = functools.reduce(traced_add, numbers, 10)
    print(f"最终结果: {result_with_initial}")

reduce_mechanics()