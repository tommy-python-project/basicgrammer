
"""
类装饰器
"""
class Counter:
    def __init__(self,func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"调用次数:{self.count}")
        return self.func(*args, **kwargs)

@Counter
def say_hello():
    print("hello")

say_hello()
say_hello()


def add_method(cls):
    def  new_method(self):
        return "新增的方法"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
print(obj.new_method())