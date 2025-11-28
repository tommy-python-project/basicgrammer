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

# 2. 数据转换管道
def data_transformation_pipeline():
    """数据转换管道"""
    print("\n=== 数据转换管道 ===")

    # 复杂数据转换
    transactions = [
        {'type': 'buy', 'amount': 100},
        {'type': 'sell', 'amount': 50},
        {'type': 'buy', 'amount': 200},
        {'type': 'sell', 'amount': 75}
    ]

    def process_transactions(acc,transaction):
        if transaction['type'] == 'buy':
            acc['total_bought'] += transaction['amount']
            acc['balance'] -= transaction['amount']
        else: # sell
            acc['total_sold'] += transaction['amount']
            acc['balance'] += transaction['amount']
        return acc

    initial_state = {
        'total_bought': 0,
        'total_sold': 0,
        'balance': 0
    }

    result = functools.reduce(process_transactions, transactions,initial_state)
    print("交易记录:", transactions)
    print("处理结果:", result)

data_transformation_pipeline()

# 3. 条件规约
def conditional_reduction():
    """条件规约"""
    print("\n=== 条件规约 ===")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 只对偶数进行累积
    def even_accumulator(acc,x):
        if x % 2 == 0:
            acc['even_sum'] += x
            acc['even_count'] += 1
        else:
            acc['odd_sum'] += x
            acc['odd_count'] += 1
        return acc

    initial = {'even_sum': 0, 'even_count': 0, 'odd_sum': 0, 'odd_count': 0}
    result = functools.reduce(even_accumulator, numbers, initial)

    print(f"数字: {numbers}")
    print(f"偶数统计 - 数量: {result['even_count']}, 总和: {result['even_sum']}")
    print(f"奇数统计 - 数量: {result['odd_count']}, 总和: {result['odd_sum']}")

conditional_reduction()





