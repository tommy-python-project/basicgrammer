"""
生成器表达式适用场景
"""
import time


# 场景1: 一次性使用数据
def process_data():
    data = (x * 2 for x in range(10))

    # 只需要遍历一次
    total = sum(data) # 直接传递给聚合函数
    print(f"总和：{total}")

    # 注意：生成器只能使用一次
    try:
        second_use = list(data)
        print(f"第二次使用: {second_use}")
    except :
        print("生成器已耗尽")

process_data()


# 场景2: 数据管道处理
def data_pipeline_demo():
    numbers = range(100)

    # 创建处理管道
    pipeline = (
        x ** 2
        for x in numbers
        if x % 2 == 0  #只处理偶数
    )

    # 继续处理管道
    filtered = (x for x in pipeline if x > 100)

    print("管道处理结果:")
    for i, result in enumerate(filtered):
        if i < 10:  # 只显示前10个
            print(result)

data_pipeline_demo()

# 场景3: 大文件处理
def process_large_file():
    # 模拟处理大文件 - 逐行处理
    lines = (f"Line {i}: Some data here" for i in range(1000000))

    # 查找包含特定关键词的行
    keyword_lines = (line for line in lines if "data" in line)

    # 只处理前几个匹配项
    count = 0
    for line in keyword_lines:
        print(line)
        count += 1
        if count >= 5:
            break

process_large_file()

"""
不适用场景
"""

# 需多次访问数据
def multiple_access_problem():
    numbers = (x for x in range(5))

    print("第一次迭代:")
    for num in numbers:
        print(num)  # 0, 1, 2, 3, 4

    print("第二次迭代:")
    for num in numbers:
        print(num)  # 没有输出！

    # 解决方面：使用列表或重新创建生成器
    numbers_list = [x for x in range(5)]
    print("列表可以多次迭代:")
    for num in numbers_list:
        print(num)
    for num in numbers_list:
        print(num)

multiple_access_problem()

def random_access_limitation():
    data_gen = (x ** 2 for x in range(10))

    # 无法直接访问特定位置
    try:
        print(data_gen[5])
    except TypeError as e:
        print(f"错误: {e}")

    # 解决方案：转换为列表或使用其他数据结构
    data_list = list(x ** 2 for x in range(10))
    print(f"第五个元素: {data_list[5]}")

random_access_limitation()


# 性能基准测试
def performance_comparison():
    large_data = range(1000000)

    # 列表推导式性能
    start_time = time.time()
    list_result = sum([x for x in large_data])
    list_time = time.time() - start_time

    # 生成器表达式性能
    start_time = time.time()
    gen_result = sum((x for x in large_data))
    gen_time = time.time() - start_time

    print(f"列表推导式时间: {list_time:.4f}秒")
    print(f"生成器表达式时间: {gen_time:.4f}秒")
    print(f"结果相同: {list_result == gen_result}")
    print(f"内存节省比例: {(list_time - gen_time) / list_time * 100:.1f}%")

performance_comparison()