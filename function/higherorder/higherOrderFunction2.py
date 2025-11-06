"""
高阶函数 map、filter()、reduce的现代替代品
"""
from functools import reduce

# 传统map()
numbers = [1,2,3,4,5]
squared = list(map(lambda x : x ** 2, numbers))
print(squared)

# 现代替代：列表推导式（更推荐）
squared = [x * 2 for x in numbers]
print(squared)

# 多个序列的map
a = [1,2,3]
b = [10,20,30]
result = list(map(lambda x,y : x + y, a, b))
print(result)

# 列表推导式替代
result = [x + y for x,y in zip(a,b)]
print(result)


"""
filter() - 现代替代：列表推导式
"""
# 传统filter()
numbers = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

# 现代替代： 列表推导式（更推荐）
evens = [x for x in numbers if x % 2 == 0]
print(evens)


"""
reduce() - 使用方式
reduce() 函数会对参数序列中的元素进行累积操作。
它将一个二元函数作用于序列的元素，每次携带一对元素（先前的结果和下一个序列元素），逐步将序列缩减为单个值。
"""

numbers = [1,2,3,4,5]
# 计算累积和
total = reduce(lambda x,y : x + y, numbers)
print(total)

# 更推荐的方式：使用内置函数
total = sum(numbers)
print(total)

# 计算累积乘积
product= reduce(lambda x,y : x * y, numbers)
print(product)

# 找最大值
maxinum = reduce(lambda x,y : x if x > y else y, numbers)
print(maxinum)

"""
何时使用map/filter,何时使用列表推导式
"""

# 简单转换，列表推导式更清晰
names = ['alice','bob','carolina']
upper_names = [name.upper() for name in names]
print(upper_names)

# 需要使用已存在的函数：map更简洁
upper_names = list(map(str.upper, names))
print(upper_names)

# 复杂逻辑：列表推导式更清晰
numbers = [1,2,3,4,5]
result = [x ** 2 for x in numbers if x % 2 == 0] # 清晰
print(result)
result = list(map(lambda x: x ** 2,filter(lambda x : x % 2 == 0, numbers)))
print(result)