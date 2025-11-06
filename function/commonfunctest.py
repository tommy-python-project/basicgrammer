
"""
高阶函数
"""
# 过滤出偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers= list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 过滤出非空字符串
word = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x != "", word))
print(non_empty)


# 使用普通函数
def is_positive(number):
    return number > 0
nums = [-2,-1,0,1,2,3]
positive_nums = list(filter(is_positive, nums))
print(positive_nums)

# 如果function为None,会过滤掉所有“假”值
mixed = [0,1,False,True,"","text",None,[]]
result = list(filter(None, mixed))
print(result)

print("==============================")
# 将所有数字平方
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# 将字符串转为大写
words= ["hello", "world", "python"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)

# 使用普通函数
def add_ten(x):
    return x + 10

nums = [1,2,3]
rest = list(map(add_ten, nums))
print(rest)

# 多个迭代对象
a = [1,2,3]
b = [10,20,30]
result = list(map(lambda x,y: x +y, a, b))
print(result)

# 实用案例：类型转换
str_numbers= ["1","2","3","4"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)

# 组合使用
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 先过滤再转换
# 找出偶数并平方
result = list(map(lambda x: x ** 2,filter(lambda x: x % 2 == 0, numbers)))
print(result)

# 使用列表推导式
even = [x for x in numbers if x % 2 == 0]
print(even)

# map 的列表推导式写法
squared = [x ** 2 for x in numbers]
print(squared)