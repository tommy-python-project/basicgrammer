"""
比较运算符
"""
from operator import itemgetter

# 排序
data = [('Alice',30),('Bob',25),('Charlie',35)]

# 使用lambda
sorted_by_age = sorted(data,key=lambda x:x[1])
print(sorted_by_age)

# 使用 operator.itemgetter(更好)
sorted_by_age = sorted(data,key= itemgetter(1))
print(sorted_by_age)