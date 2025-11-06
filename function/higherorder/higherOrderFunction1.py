"""
高阶函数 - 接受函数作为参数
"""



# 定义一个高阶函数
def apply_operation(numbers, operation):
    """对列表中的每个数字应用操作"""
    return [operation(num) for num in numbers]

# 定义一些普通函数
def square(x):
    return x ** 2

def double(x):  # 添加：定义 double 函数
    return x * 2

# 使用高阶函数
numbers = [1, 2, 3, 4, 5]
print(apply_operation(numbers, square))
print(apply_operation(numbers, double))


def make_multiplier(n):
    """返回一个将参数乘以n的函数"""
    def multiplier(x):
        return x * n
    return multiplier

# 创建不同的乘法器
times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))
print(times5(10))

"""
常见的高阶函数
"""

# sorted() 接受key 参数（函数）
fruits = ["apple", "banana", "cherry","date"]
sorted_by_length = sorted(fruits, key=len)
print(sorted_by_length)

# 按最后一个字母排序
sorted_by_last = sorted(fruits,key = lambda x : x[-1])
print(sorted_by_last)