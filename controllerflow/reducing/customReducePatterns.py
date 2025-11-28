"""
自定义规约模式
"""
import functools


def custom_reduce_patterns():
    """自定义规约模式"""
    print("\n=== 自定义规约模式 ===")

    # 实现 group_by 功能
    def group_by(key_func,sequence):
        def reducer(acc,item):
            key = key_func(item)
            if key not in acc:
                acc[key] = []
            acc[key].append(item)
            return acc
        return functools.reduce(reducer, sequence, {})

    # 测试数据
    students = [
        {'name': 'Alice','grade':'A'},
        {'name': 'Bob','grade':'B'},
        {'name': 'Charlie','grade':'A'},
        {'name': 'David','grade':'C'},
        {'name': 'Eve','grade':'B'},
    ]

    grouped = group_by(lambda s: s['grade'], students)
    print("按成绩分组:")
    for grade,students_in_grade in grouped.items():
        names = [s['name'] for s in students_in_grade]
        print(f"  成绩{grade}: {names}")

    # 实现频率统计
    def frequency(sequence):
        def reducer(acc,item):
            acc[item] = acc.get(item, 0) + 1
            return acc
        return functools.reduce(reducer, sequence, {})

    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    freq = frequency(words)
    print(f"\n词频统计: {freq}")

custom_reduce_patterns()


# 2. 可组合的规约操作
def composable_reductions():
    """可组合的规约操作"""
    print("\n=== 可组合规约操作 ===")

    # 定义可重用的规约函数
    def make_sum_reducer():
        return lambda a,b: a+b

    def make_product_reducer():
        return lambda a,b: a*b

    def make_max_reducer():
        return lambda a, b: a if a > b else b

    # 组合使用
    numbers = [1,2,3,4,5]

    operations = [
        ('求和',make_sum_reducer()),
        ('求积',make_product_reducer()),
        ('最大值',make_max_reducer())
    ]

    for name,reducer in operations:
        result = functools.reduce(reducer, numbers)
        print(f"{name}: {result}")

    # 链式规约
    def chain_reductions(reducers, sequence, initial=None):
        result = sequence
        for reducer in reducers:
            if initial is not None:
                result = functools.reduce(reducer, result, initial)
            else:
                result = functools.reduce(reducer, result)
        return result

    # 先求和再乘以 2 （演示用途）
    reducers = [
        lambda a,b: a+b,
        lambda total: total * 2  # 注意：这个不是规约函数，需要调整
    ]

    # 正确的链式操作
    sum_result = functools.reduce(lambda a,b: a+b, numbers)
    final_result = sum_result * 2
    print(f"链式操作结果: {final_result}")

composable_reductions()