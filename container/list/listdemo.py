

def listdemo():
    names = ["tom", "jerry", "shuke", "beita"]
    # print(names)
    # names.append("jack")
    # print(names)
    # names.insert(1, "json")
    # print(names)
    # names.extend(["marry","jan"])
    # print(names)

    # names.sort()
    # print(names)
    #
    # names[2] = "jackson"
    # print(names)
    #
    # names.remove("jackson")
    # print(names)
    # names.pop()
    # print(names)
    # names.pop(2)
    # print(names)
    # names.clear()
    # print(names)
    # del names
    # # print(names)

    # 列表推导式
    squares = [i ** 2 for i in range(5)]
    print(squares)  # [0, 1, 4, 9, 16]

    numbers = [1, 2, 3, 4, 5,6, 7, 8, 9]
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(even_numbers)  # [2, 4, 6, 8]

    # 只保留长度大于3的字符串
    names = ["tom", "jerry", "shuke", "beita"]
    long_names = [name for name in names if len(name) > 3]
    print(long_names)  # ['jerry', 'shuke', 'beita']

    ## 条件表达式（三元运算）
    # 如果是偶数则平方，如果是奇数则立方
    numbers = [1, 2, 3, 4, 5]
    result = [x**2 if x % 2== 0 else x**3 for x in numbers]
    print(result)

    # 字符串处理：长度大于3的转大写，否则转小写
    names = ["tom", "jerry", "shuke", "beita"]
    processed = [name.upper() if len(name) > 3 else name.lower() for name in names]
    print(processed)  # ['tom', 'JERRY', 'SHUKE', 'BEITA']


    # 两个列表的组合
    colors = ["red","green"]
    sizes = ["S","M","L"]
    combinations = [(color,size) for color in colors for size in sizes]
    print(combinations)

    # 矩阵转置
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose = [[row[i] for row in matrix] for i in range(3)]
    print(transpose)

    # 从字典中提取值
    person = {"name":"Alice", "age":25,"city":"beijing"}
    values = [value for value in person.values()]
    print(values)

    # 过于复杂的推导式（不推荐）
    complex_result = [x**2 if x % 2 == 0 else x**3 for x in range(10) if x > 2 if x < 8]
    print(complex_result)
    # 可读性更好的方式（推荐）
    result = []
    for x in range(10):
        if 2 < x  < 8:
            if x %2 == 0:
                result.append(x**2)
            else :
                result.append(x**3)
    print(result)



if __name__ == '__main__':
    listdemo()

