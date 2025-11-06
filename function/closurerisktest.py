"""
闭包陷阱1 - 循环中的闭包陷阱
"""
from functools import partial


# 错误示例
def create_multiplies():
    return [lambda x : i * x for i in range(5)]

multiplies = create_multiplies()
print(multiplies[2](10))  # 期望 20 ，实际输出 40
# 原因：所有闭包共享同一个变量 i，循环结束后 i= 4

# 正确做法1 ： 使用默认参数
def create_multiplies():
    return [lambda x,i = i: i * x for i in range(5)]
multiplies = create_multiplies()
print(multiplies[2](10))

# 正确做法2:使用functools.partial
def multiply(x, y):
    return x * y

def create_multiplies():
    return [partial(multiply,i) for i in range(5)]
multiplies = create_multiplies()
print(multiplies[2](10))