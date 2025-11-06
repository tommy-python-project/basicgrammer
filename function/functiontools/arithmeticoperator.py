"""
算术运算符
"""
from functools import reduce
from arithmeticoperator import add, mul

# 替代lambda
numbers = [1,2,3,4,5]

# 使用 lambda
total = reduce(lambda x, y: x + y, numbers)

# 使用 operator (更清晰)
total = reduce(add, numbers)
print(total)

product = reduce(mul, numbers)
print(product)