"""
性能对比
"""
import functools
import time


def performance_comparison():
    """性能对比"""
    print("\n==== 性能对比 ====")

    large_data = list(range(10000))

    # 方法1: reduce
    start_time = time.time()
    result1 = functools.reduce(lambda a, b: a + b, large_data)
    time1 = time.time() - start_time

    # 方法2: 内置sum
    start_time = time.time()
    result2 = sum(large_data)
    time2 = time.time() - start_time

    # 方法3: 循环
    start_time = time.time()
    result3 = 0
    for x in large_data:
        result3 += x
    time3 = time.time() - start_time

    print(f"reduce 时间: {time1:.6f}秒")
    print(f"sum    时间: {time2:.6f}秒")
    print(f"循环   时间: {time3:.6f}秒")
    print(f"结果相同: {result1 == result2 == result3}")

performance_comparison()

"""
错误处理和边界情况
"""

def error_handling():
    """错误处理和边界情况"""
    print("\n=== 错误处理 ===")

    # 空序列处理
    try:
        result = functools.reduce(lambda a, b: a + b, [])
        print(f"空序列结果: {result}")
    except TypeError as e:
        print(f"空序列错误: {e}")

    # 提供初始值处理空序列
    result_with_initial = functools.reduce(lambda a, b: a + b, [],0)
    print(f"空序列带初始值: {result_with_initial}")

    # 单元素序列
    single_element = functools.reduce(lambda a, b: a + b, [42])
    print(f"单元素序列: {single_element}")

    # 类型不匹配处理
    def safe_add(a, b):
        try:
            return a + b
        except TypeError:
            return f"({a},{b})"

    mixed_data = [1, 'hello', 3.14]
    result = functools.reduce(safe_add, mixed_data)
    print(f"混合类型处理: {result}")

error_handling()