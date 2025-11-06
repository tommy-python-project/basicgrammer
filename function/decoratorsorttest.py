"""
多个装饰器执行顺序
多个装饰器从下往上应用，从上往下执行
"""

def decorator1(func):
    print("应用 decorator1")
    def wrapper(*args, **kwargs):
        print("执行decorator1")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    print("应用 decorator2")

    def wrapper(*args, **kwargs):
        print("执行decorator2")
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def my_function():
    print("执行 my_function")

print("---调用函数---")
my_function()