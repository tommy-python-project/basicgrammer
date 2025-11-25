"""
常见规约模式
"""
import functools


# 1. 累积计算
def cumulative_calculations():
    """累积计算模式"""
    print("\n=== 累积计算 ===")

    # 计算阶乘
    def factorial(n):
        return functools.reduce(lambda a,b: a * b, range(1, n + 1))

    for i in range(1,6):
        print(f"{i}! = {factorial(i)}")

    # 计算字符串连接
    words = ['Hello','World','Python','Programming']
    concatenated = functools.reduce(lambda a,b: a + '' + b, words)
    print(f"字符串连接: '{concatenated}'")

    # 计算数字拼接
    digits = [1,2,3,4,5]
    number = functools.reduce(lambda a,b: a * 10 + b, digits)
    print(f"数字拼接: {digits} -> {number}")

cumulative_calculations()

# 2. 查找和比较
def search_and_comparison():
    """查找和比较模式"""
    print("\n=== 查找和比较 ===")

    numbers = [3, 1, 4, 1, 5, 9, 2, 6]

    # 自定义最大值查找
    def custom_max(a,b):
        return a if a > b else b

    max_value = functools.reduce(custom_max, numbers)
    print(f"最大值: {max_value}")

    # 自定义最小值查找
    min_value = functools.reduce(lambda a,b: a if a < b else b, numbers)
    print(f"最小值: {min_value}")

    # 查找最长字符串
    strings = ['apple','banana','cherry','date']
    longest = functools.reduce(lambda a,b: a if len(a) > len(b) else b, strings)
    print(f"最长字符串: '{longest}'")

search_and_comparison()

"""
3. 聚合统计
"""


def aggregation_statistics():
    """聚合统计模式"""
    print("\n=== 聚合统计 ===")

    # 数据点
    data = [23, 17, 35, 28, 19, 31, 26]

    # 计算平均值
    def average_calc(acc, x):
        acc['sum'] += x
        acc['count'] += 1
        acc['mean'] = acc['sum'] / acc['count']
        return acc

    initial = {'sum': 0, 'count': 0, 'mean': 0}
    result = functools.reduce(average_calc, data, initial)
    print(f"数据: {data}")
    print(f"平均值: {result['mean']:.2f}")
    print(f"总和: {result['sum']}")
    print(f"数量: {result['count']}")

    # 计算方差
    def variance_calc(acc, x):
        acc['sum'] += x
        acc['sum_sq'] += x ** 2
        acc['count'] += 1
        return acc

    var_initial = {'sum': 0, 'sum_sq': 0, 'count': 0}
    var_result = functools.reduce(variance_calc, data, var_initial)
    mean = var_result['sum'] / var_result['count']
    variance = (var_result['sum_sq'] / var_result['count']) - mean ** 2
    print(f"方差: {variance:.2f}")


aggregation_statistics()