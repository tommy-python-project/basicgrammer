"""
标准库中的生成器函数
"""
import itertools

# 1. 用于筛选的生成器函数
print("========用于筛选的生成器函数==========")

# filterfalse - 筛选不符合条件的元素
numbers = [1,2,3,4,5]
result = itertools.filterfalse(lambda x: x % 2 == 0, numbers)
print(list(result))

# dropwhile - 丢弃元素直到条件为False
result = itertools.dropwhile(lambda x: x < 3, numbers)
print(list(result))

# takewhile - 获取元素直到条件为False
result = itertools.takewhile(lambda x: x < 4, numbers)
print(list(result))


print("========用于映射的生成器函数==========")
# 2. 用于映射的生成器函数

# accumulate - 累计计算
result = itertools.accumulate(numbers)
print(list(result))

# starmap - 对可迭代对象的每个元素应用函数
pairs = [(2,3),(4,5),(6,7)]
result = itertools.starmap(lambda x,y: x * y, pairs)
print(list(result))


print("========用于合并的生成器函数==========")

# 3. 用于合并的生成器函数

# chain - 连接多个可迭代对象
list1 = [1,2,3]
list2 = [4,5,6]
result = itertools.chain(list1, list2)
print(list(result))

# zip_longest - 最长的可迭代对象决定长度
name = ['Alice','Bob','Charlie']
age = [25,30]
result = itertools.zip_longest(name,age,fillvalue = '未知')
print(list(result))