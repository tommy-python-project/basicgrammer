

def test():
    s1 = {1,2,3,4,5,6,7,8}
    s2 = {5,6,7,8,9,10}

    # 获取差集
    print(s1.difference(s2))  # 标准操作
    print(s1 - s2)  # 快捷操作

    # 获取交集
    print(s1.intersection(s2)) # 标准操作
    print(s1 & s2) # 快捷操作

    # 获取并集
    print(s1.union(s2))  # 标准操作
    print(s1 | s2) # 快捷操作

    # 获取真实差集
    print(s1.symmetric_difference(s2))  # 标准操作
    print(s1 ^ s2)  # 快捷操作


if __name__ == '__main__':
    test()