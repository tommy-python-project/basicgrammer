"""
functools模块常用功能
"""
from functools import reduce, lru_cache, wraps

# 1. reduce - 累积操作
numbers = [1,2,3,4,5]
total = reduce(lambda x,y: x+y, numbers)
print(total)

# 2. lru_cache - 缓存装饰器
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(100))

# 3. wraps - 保留原函数元数据
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greet someone"""
    print("Hello", name)
print(greet.__doc__)
print(greet.__name__) 
