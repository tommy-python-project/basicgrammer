"""
不同方法生成等差数列的性能对比
"""
import itertools
import time

from controllerflow.generator.arithmeticSequence import arithmetic_sequence


def performance_benchmark():
    """不同方法生成等差数列的性能对比"""

    n = 10000

    # 方法1: range + list
    start = time.time()
    result1 = list(range(0,n,2))
    time1 = time.time() - start

    # 方法2: 自定义生成器
    start = time.time()
    result2 = list(arithmetic_sequence(0,n,2))
    time2 = time.time() - start

    # 方法3: itertools.count + islice
    start = time.time()
    result3 = list(itertools.islice(itertools.count(0,2),n //2))
    time3 = time.time() - start

    print("性能对比 (生成100,000个元素的等差数列):")
    print(f"range + list: {time1:.6f}秒")
    print(f"自定义生成器: {time2:.6f}秒")
    print(f"itertools: {time3:.6f}秒")
    print(f"结果相同: {result1 == result2 == result3}")

performance_benchmark()