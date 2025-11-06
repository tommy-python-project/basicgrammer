"""
zip()函数
"""

# 两个列表打包
names = ["Alice", "Bob", "Charlie"]
ages = [18, 19, 20, 20]
result = list(zip(names, ages))
print(result)

# 三个列表打包
cities = ["Beijing", "Shanghai", "Shenzhen"]
result = list(zip(names,ages,cities))
print(result)

# zip() 会以最短的序列为准
list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c']
result = list(zip(list1, list2))
print(result)

"""
常见应用场景
"""
# 1. 创建字典
keys = ["name", "age", "city"]
values = ["Alice", 25, "beijing"]
result = dict(zip(keys, values))
print(result)

# 2. 并行遍历多个列表
names = ["Alice", "Bob", "Charlie"]
scores = [85,90,78]
for name,score in zip(names, scores):
    print(f"{name}的分数是{score}")

# 3. 矩阵转置
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# 转置矩阵（行变列，列变行）
transposed = list(zip(*matrix))
print(transposed)

# 如果想要列表而不是元组
transposed = [ list(row) for row in zip(*matrix)]
print(transposed)

print("=======解压（反向操作）=======")
# 4. 解压（反向操作）
pairs = [("Alice",25),("Bob",30),("Charlie",35)]
# 使用 * 和 zip解压
names,ages = zip(*pairs)
print(names)
print(ages)

names = list(names)
ages = list(ages)
print(names)
print(ages)

print("=======配对元素进行计算=======")
prices = [10,20,30,40]
quantities = [2,3,1,5]
# 计算总价
total= sum(p * q for p,q in zip(prices, quantities))
print(total)

print("=======比较两个列表=======")
list1 = [1,2,3,4,5]
list2 = [1,2,4,4,6]
difference = [(i,a,b) for i,(a,b) in enumerate(zip(list1, list2)) if a != b]
print(difference)

# 与enumerate()结合
names = ["Alice", "Bob", "Charlie"]
ages = [18, 19, 20]
# 同时获取索引
for index,(name,age) in enumerate(zip(names, ages)):
    print(f"{index}: {name} is {age} years old")


print("=======Python 3.10+ 的strict参数=======")
list1 = [1,2,3]
list2 = ['a', 'b']

try:
    result = list(zip(list1, list2,strict=True))
except ValueError as e:
    print(f"错误：{e}")

"""
实用技巧
"""
print("=======1 交换字典的键值=======")
original = {'a':1,'b':2,'c':3}
swapped = dict(zip(original.values(), original.keys()))
print(swapped)

print("=======2 分组相邻元素=======")
numbers = [1, 2, 3, 4, 5, 6]
pairs = list(zip(numbers[::2], numbers[1::2]))
print(pairs)

print("=======3 创建滑动窗口=======")
data = [1, 2, 3, 4, 5]
window = list(zip(data, data[1:], data[2:]))
print(window)
