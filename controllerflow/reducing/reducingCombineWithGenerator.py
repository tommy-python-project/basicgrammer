"""
与生成器结合使用
"""
import functools
import itertools


# 1. 惰性规约
def lazy_reduction():
    """惰性规约"""
    print("\n=== 惰性规约 ===")

    # 生成器表达式 + reduce
    def expensive_operation(x):
        print(f"计算: {x}")
        return x ** 2

    # 惰性计算
    numbers = (expensive_operation(x) for x in range(1, 6))
    total = functools.reduce(lambda a, b: a + b, numbers)
    print(f"总和: {total}")

    # 对比： 立即计算
    print("\n立即计算版本:")
    numbers_list = [expensive_operation(x) for x in range(1, 6)]
    total_list = functools.reduce(lambda a, b: a + b, numbers_list)
    print(f"总和: {total_list}")

lazy_reduction()


# 2. 无限序列规约
def infinite_sequence_reduction():
    """无限序列规约（有限截取）"""
    print("\n=== 无限序列规约 ===")

    # 生成无限序列但只取一部分
    infinite_numbers = itertools.count(1)
    limited = itertools.islice(infinite_numbers,5) # 只取前5个

    product = functools.reduce(lambda a, b: a * b, limited)
    print(f"前5个自然数的乘积: {product}")

    # 斐波那契数列规约
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib_sequence = itertools.islice(fibonacci(), 10) # 前10个斐波那契数列
    fib_sum = functools.reduce(lambda a, b: a + b, fib_sequence)
    print(f"前10个斐波那契数之和: {fib_sum}")

infinite_sequence_reduction()

