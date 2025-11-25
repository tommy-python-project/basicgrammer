"""
自定义等差数列生成器
"""

def arithmetic_sequence(start, stop=None, step=1):
    """
    生成等差数列
    :param start: 起始值（如果stop为None，则从0开始到start）
    :param stop:  结束值（不包含）
    :param step:  步长
    :return:
    """
    if stop is None:
        start, stop = 0, start

    current = start
    while (step > 0 and current < stop) or (step < 0 and current >= stop):
        yield current
        current += step

def arithmetic_demo():
    print("=== 基础等差数列 ===")
    seq1 = arithmetic_sequence(5)
    print(f"0到5: {list(seq1)}")

    # 2, 4, 6, 8
    seq2 = arithmetic_sequence(2, 10, 2)
    print(f"2到10步长2: {list(seq2)}")

    # 10, 7, 4, 1
    seq3 = arithmetic_sequence(10, 0, -3)
    print(f"10到0步长-3: {list(seq3)}")

arithmetic_demo()
