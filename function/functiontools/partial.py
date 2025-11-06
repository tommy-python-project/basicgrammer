"""
partial 函数用于固定函数的部分参数，创建新的可调用对象
"""
from functools import partial
from operator import add, mul, methodcaller
from sys import prefix

from function.commonfunctest import even_numbers

"""
一、基本用法
"""

# 原始函数
def multiply(x,y):
    return x * y

# 冻结第一个参数
double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(5))  # 输出10 (2 * 5)
print(triple(5))  # 输出15 (3 * 5)

# 冻结第二个参数
multiply_by_10 = partial(multiply, y = 10)
print(multiply_by_10(7))


"""
二、实际应用场景
"""

"""
1. 数学运算
"""

# 基础教学函数
def power(base,exponent):
    return base ** exponent

def divide(dividend,divisor):
    return dividend / divisor

# 创建特定函数
square = partial(power, exponent = 2)
cube = partial(power, exponent = 3)
sqrt = partial(power, exponent = 0.5)

half = partial(divide, divisor = 2)
quarter = partial(divide, divisor = 4)

print(f"5的平方:{square(5)} ")
print(f"3的立方:{cube(3)} ")
print(f"16的平方根: {sqrt(16)} ")
print(f"10的一半: {half(10)} ")

"""
2. 字符串处理
"""

# 原始字符串处理函数
def process_text (text,prefix = "",suffix = "",uppercase = False):
    result = text
    if uppercase:
        result = result.upper()
    return f"{prefix}{result}{suffix}"

# 创建特定处理器
add_quotes = partial(process_text,prefix='"',suffix='"')
make_title = partial(process_text,uppercase=True)
add_brackets = partial(process_text,prefix='[',suffix=']')

text = "hello world"
print(add_quotes(text))
print(make_title(text))
print(add_brackets(text))

# 组合使用
fancy_format= partial(process_text,prefix='*** ',suffix=' ***',uppercase=True)
print(fancy_format(text))

"""
3. 数据处理和过滤
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 创建特定的过滤函数
def is_divisible(number,divisor):
    return number % divisor == 0

is_even = partial(is_divisible,divisor = 2)
is_odd = partial(is_divisible,divisor = 2) # 配合filter使用
is_multiple_of_3 = partial(is_divisible,divisor = 3)
is_multiple_of_5 = partial(is_divisible,divisor = 5)

# 使用过滤
even_numbers = list(filter(is_even, numbers))
multiples_of_3 = list(filter(is_multiple_of_3,numbers))
multiples_of_5 = list(filter(is_multiple_of_5, numbers))

print("偶数:", even_numbers)
print("3的倍数:", multiples_of_3)
print("5的倍数:", multiples_of_5)

# 奇数 （使用lambda 配合partial）
odd_numbers = list(filter(lambda x : not is_even(x), numbers))
print("奇数:", odd_numbers)


"""
4. 配置和默认值
"""

# 模拟API 调用函数
def api_call(endpoint,method = "GET",timeout = 30,headers =None):
    print(f"调用 {method} {endpoint}, 超时: {timeout}s, 头信息: {headers}")
    # 实际中这里会是 requests.request(method, endpoint, timeout=timeout, headers=headers)
    return f"{method} {endpoint}"

# 创建特定配置的 API 客户端
default_api = partial(api_call, timeout=60, headers={'User-Agent': 'MyApp'})
fast_api = partial(api_call, timeout=5)
secure_api = partial(api_call, headers={'Authorization': 'Bearer token'})

# 使用
print(default_api('/users'))
print(fast_api('/status', method='POST'))
print(secure_api('/admin', method='DELETE'))


"""
5. 与map和filter结合
"""

data = [
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 30, 'score': 92},
    {'name': 'Charlie', 'age': 22, 'score': 78},
    {'name': 'Diana', 'age': 28, 'score': 95}
]

# 创建特定的键获取函数
def get_attribute(item,key):
    return item[key]

get_name = partial(get_attribute, key='name')
get_age = partial(get_attribute, key='age')
get_score = partial(get_attribute, key='score')

# 提取数据
names = list(map(get_name, data))
ages = list(map(get_age, data))
scores = list(map(get_score, data))

print("姓名:", names)
print("年龄:", ages)
print("分数:", scores)

# 过滤函数
def score_above (item,threshold):
    return item['score'] > threshold

high_scores = partial(score_above, threshold=90)
young_people = partial(score_above, threshold=80)
high_scorers = list(filter(high_scores, data))
print("高分学生:",[p['name'] for p in high_scorers])

"""
6. 类方法和实例方法
"""

class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def add(self, x, y=None):
        if y is None:
            self.value += x
        else:
            self.value = x + y
        return self.value

    def multiply(self, x, y=None):
        if y is None:
            self.value *= x
        else:
            self.value = x * y
        return self.value

# 创建计算器实例
calc = Calculator(10)

# 冻结实例方法的部分参数
add_five = partial(calc.add, 5)
multiply_by_three = partial(calc.multiply, 3)

print(add_five())
print(add_five())
print(multiply_by_three())

# 冻结两个参数（静态使用）
static_add = partial(Calculator.add, y=5)  # 这里需要创建新实例
calc2 = Calculator()
result = static_add(calc2, 10)  # 需要传递 self
print(result)  # 15


"""
7. 回调函数和事件处理
"""

class Button:
    def __init__(self, label):
        self.label = label
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def click(self):
        if self.callback:
            self.callback(self.label)

def handle_click(button_label,user_role,log_message):
    print(f"用户 {user_role} 点击了按钮 '{button_label}': {log_message}")

# 创建特定角色的处理器
admin_handler = partial(handle_click, user_role="管理员", log_message="执行管理操作")
user_handler = partial(handle_click, user_role="普通用户", log_message="执行用户操作")
guest_handler = partial(handle_click, user_role="访客", log_message="查看信息")

# 设置按钮回调
save_button = Button("保存")
delete_button = Button("删除")
view_button = Button("查看")

save_button.set_callback(admin_handler)
delete_button.set_callback(user_handler)
view_button.set_callback(guest_handler)

# 模拟点击
save_button.click()  # 用户 管理员 点击了按钮 '保存': 执行管理操作
delete_button.click() # 用户 普通用户 点击了按钮 '删除': 执行用户操作
view_button.click()  # 用户 访客 点击了按钮 '查看': 查看信息


"""
8. 数据库查询构建
"""

def build_query(table,fields='*',where=None,order_by=None,limit=None):
    query = f"SELECT {fields} FROM {table}"

    if where:
        query += f" WHERE {where}"
    if order_by:
        query += f" ORDER BY {order_by}"
    if limit:
        query += f" LIMIT {limit}"
    return query

# 创建特定表的查询构建器
user_query = partial(build_query,'users')
product_query = partial(build_query, 'products')
order_query = partial(build_query, 'orders')

# 创建特定类型的查询
user_basic = partial(user_query, fields='id, name, email')
recent_products = partial(product_query, order_by='created_at DESC', limit=10)
active_orders = partial(order_query, where='status = "active"')

print(user_basic()) # SELECT id, name, email FROM users


print(recent_products()) # SELECT * FROM products ORDER BY created_at DESC LIMIT 10

print(active_orders(limit=5)) # SELECT * FROM orders WHERE status = "active" LIMIT 5


"""
9. 与operator模块结合
"""

# 结合operator创建强大的函数组合
numbers = [1,2,3,4,5]

# 数学运算
add_five = partial(add, 5)
multiply_by_three = partial(mul, 3)

result1 = list(map(add_five, numbers))
result2 = list(map(multiply_by_three, numbers))

print("加5:", result1)
print("乘3:", result2)

# 结合 methodcaller
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, greeting, punctuation):
        return f"{greeting}, {self.name}{punctuation}"

people = [Person('Alice'), Person('Bob')]


# 创建特定的问候方式
formal_greet = partial(methodcaller('greet', 'Hello', '!'))
casual_greet = partial(methodcaller('greet', 'Hi', '...'))

formal_greetings = list(map(formal_greet, people))
casual_greetings = list(map(casual_greet, people))

print("正式问候:", formal_greetings)   # ['Hello, Alice!', 'Hello, Bob!']
print("随意问候:", casual_greetings)   # ['Hi, Alice...', 'Hi, Bob...']


"""
三、高级技巧
"""

"""
1. 部分应用的可变参数
"""

def flexible_function(a,b,*args,**kwargs):
    result = f"a={a},b={b}"
    if args:
        result += f", args={args}"
    if kwargs:
        result += f", kwargs={kwargs}"
    return result

# 部分应用可以处理可变参数
part1 = partial(flexible_function,1,2)
part2 = partial(flexible_function,1,2,3,4)
part3 = partial(flexible_function,1,2,x=10,y=20)

print(part1())
print(part1(5, 6, z=30))
print(part2())
print(part3())

"""
2. 组合使用多个partial
"""

def complex_operation(a,b,c,d,e):
    return a + b * c - d / e

# 逐步冻结参数
step1 = partial(complex_operation,10) ## 冻结 a=10
step2 = partial(step1, 2)                   # 冻结 b=2
step3 = partial(step2, 3)                   # 冻结 c=3
step4 = partial(step3, 4)                   # 冻结 d=4

result = step4(2)  # 提供最后一个参数 e=2
print(result)      # 10 + 2*3 - 4/2 = 10 + 6 - 2 = 14
