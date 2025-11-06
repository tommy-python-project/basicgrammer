"""
9种可调用对象 - "可调用对象"是指任何可以通过函数调用运算符 () 来调用的对象。
"""
import asyncio

"""
1. 内置函数 (Built-in Functions)
Python解释器内置的函数，用C语言实现。
"""
# 内置函数示例
print("Hello, World!")  # print是内置函数
len([1, 2, 3])         # len是内置函数
max(1, 2, 3)           # max是内置函数

"""
2. 内置方法 (Built-in Methods)
特定于某些内置类型的方法。
"""
my_list = [1, 2, 3]
my_list.append(4)

my_dict = {'a': 1}
my_dict.get('b', 0)

"""
3- 用户定义函数 (User-defined Functions)
使用 def 关键字定义的函数。
"""
def greet(name):
    return f"Hello, {name}!"

result = greet("Jim")
print(result)

"""
4. 方法 (Methods)
在类中定义的函数，与特定实例关联。
"""
class MyClass:

    def instance_method(self,x):
        return x * 2

    @classmethod
    def class_method(cls):
        return "class method"

    @staticmethod
    def static_method():
        return "static method"

obj = MyClass()
obj.instance_method(5)    # 实例方法
MyClass.class_method()    # 类方法
MyClass.static_method()   # 静态方法

"""
5. 类
调用类会创建该类的实例（调用类的 __new__ 和 __init__ 方法）。
"""
class Person:
    def __init__(self, name):
        self.name = name

# 调用类来创建实例
person = Person("Jim")
print(person.name)

"""
6-类的实例
如果类定义了 __call__ 方法，那么它的实例就是可调用的。
"""

class Adder:

    def __init__(self,n):
        self.n = n

    def __call__(self, x):
        return self.n + x

# 创建实例
add_five = Adder(5)
# 调用实例
result = add_five(10) # 相当于 add_five.__call__(10)
print(result)


"""
7. 生成器函数 (Generator Functions)
包含 yield 语句的函数，调用时返回生成器对象。
"""
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# 调用生成器函数
counter = count_up_to(5) # 返回生成器对象
for num in counter:
    print(num)

"""
8. 协程函数 (Coroutine Functions)
使用 async def 定义的函数，调用时返回协程对象。
"""

async def async_greet(name):
    await asyncio.sleep(1)
    return f"Hello, {name}!"

# 调用协程函数
coroutine = async_greet("Alice") # 返回写成对象

"""
9-lambda函数
匿名函数，使用 lambda 关键字创建。
"""
square = lambda x: x ** 2
result = square(4)
print(result)

# 直接在需要的地方使用
numbers = [1, 2, 3,4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)


"""
检测可调用函数
使用callable() 函数来检测对象是否可调用
"""
def test_callable():
    pass

class MyClass:
    def __init__(self):
        pass

obj = MyClass()
print(callable(test_callable))  # True
print(callable(MyClass))
print(callable(obj))            # False
print(callable("hello"))        # False
print(callable([1, 2, 3]))      # False