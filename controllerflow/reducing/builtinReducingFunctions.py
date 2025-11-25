"""
内置规约函数
"""

def builtin_reducing_functions():
    """Python内置规约函数演示"""
    print("=== 内置规约函数 ===")

    numbers = [1,2,3,4,5]

    # sum - 求和
    total = sum(numbers)
    print(f"sum({numbers}) = {total}")

    # min/max - 最小/最大值
    print(f"min(numbers) = {min(numbers)})")
    print(f"max(numbers) = {max(numbers)})")

    # all -所有元素为真
    bool_list = [True, True,False, True]
    print(f"all({bool_list}) = {all(bool_list)})")

    # any - 任一元素为真
    print(f"any({bool_list}) = {any(bool_list)})")

    # len - 长度（字符串、列表等）
    print(f"len('hello') = {len('hello')}")

builtin_reducing_functions()