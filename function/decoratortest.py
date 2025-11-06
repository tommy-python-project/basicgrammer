"""
装饰器
"""
from functools import wraps


def greet(name):
    return f"Hello, {name}!"

# 函数可以赋值给变量
say_hello = greet
print(say_hello("Alice"))

# 函数可以作为参数传递
def call_func(func,value):
    return func(value)
print(call_func(greet,"Alice"))


# 最简单的装饰器
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

def say_hello():
    print("Hello")

# 手动应用装饰器
say_hello = my_decorator(say_hello)
say_hello()

# 使用@语法糖
print("==========使用语法糖===========")
@my_decorator
def say_hello():
    print("Hello")
say_hello()

# 装饰带参数的函数
print("==========装饰带参数的函数===========")
# 使用*args 和 **kwargs来处理任意参数：
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}函数")
        result = func(*args, **kwargs)
        print(f"函数返回：{result}")
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a + b

@my_decorator
def greet(name,greeting="Hello"):
    return f"{greeting}, {name}!"
print(add(3,5))
print(greet("Alice",greeting="Hi"))


print("==========保留函数元信息===========")
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """这是wrapper的文档"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """这是example的文档"""
    pass

print(example.__name__)
print(example.__doc__)


print("==========带参数的装饰器===========")
def repeat(times):
    """让函数重复执行times次的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")