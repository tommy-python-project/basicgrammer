"""
lambda 函数
"""
add_lambda = lambda x,y : x+y
print(add_lambda(3,5))

square = lambda x : x ** 2
print(square(3))

# 配合map使用
numbers = [1, 2, 3, 4, 5]
squared= list(map(lambda x: x ** 2,numbers))
print(squared)

# 配合filter使用
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 配合sorted使用
students = [('Alice',85),('Bob',75),('Charlie',90)]
sorted_students = sorted(students, key=lambda x:x[1])
print(sorted_students)

# 在数据结构中使用
operations = {
    'add': lambda x,y: x + y,
    'subtract': lambda x,y : x -y,
    'multiply': lambda x,y: x * y,
}
print(operations['add'](10,5))
print(operations['multiply'](10,5))

# 可以使用三元表达式
max_value = lambda x,y : x if x > y else y
print(max_value(10,5))


