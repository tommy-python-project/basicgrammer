"""
高级规约应用
"""
import functools


# 1. 嵌套数据结构处理
def nested_data_processing():
    """嵌套数据结构处理"""
    print("\n=== 嵌套数据处理 ===")

    # 处理嵌套列表
    nested_lists = [[1,2,3],[4,5],[6,7,8,9]]

    # 展平嵌套列表
    flattened = functools.reduce(lambda a,b:a + b, nested_lists)
    print(f"嵌套列表: {nested_lists}")
    print(f"展平结果: {flattened}")

    # 合并多个字典
    dicts = [
        {'a': 1,'b':2},
        {'c':3,'d':4},
        {'e':5,'a':10} # 注意键重复
    ]

    def merge_dicts(a, b):
        return {**a, **b}  # 后面的字典覆盖前面的

    merged = functools.reduce(merge_dicts, dicts)
    print(f"合并字典: {merged}")

nested_data_processing()


