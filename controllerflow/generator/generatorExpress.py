"""
生成器表达式 vs 列表推导式对比
"""
import sys


def memory_comparison():
    # 大数据的对比
    large_range = range(1000000)

    # 列表推导式 -占用大量内存
    list_result = [x ** 2 for x in large_range]
    print(f"列表推导式内存: {sys.getsizeof(list_result)} bytes")  # 约 8.5MB

    # 生成器表达式 -- 几乎不占内存
    gen_result = (x ** 2 for x in large_range)
    print(f"生成器表达式内存: {sys.getsizeof(gen_result)} bytes")

    # 验证结果相同
    print(f"前5个元素相同: {list(gen_result)[:5] == list_result[:5]}")

memory_comparison()
