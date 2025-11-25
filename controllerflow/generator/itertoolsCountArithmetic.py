"""
itertools.count - 无限数列
"""
import itertools


def itertools_count_demo():
    print("=== itertools.count 无限数列 ===")

    # 从 10开始，步长尾2的无限数列
    counter = itertools.count(10,2)

    print("前10个元素:")
    for i, num in enumerate(counter):
        if i >= 10:
            break
        print(num, end=" ")
    print()

    # 与zip结合使用
    items = ['a', 'b', 'c', 'd']
    numbered = zip(itertools.count(1), items)
    print(f"带编号的列表: {list(numbered)}")

itertools_count_demo()

