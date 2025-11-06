"""
描述符
"""

class Validator:

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, obj, objtype=None):
        """获取属性值时调用"""
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        """设置属性值时调用"""
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value must be <= {self.max_value}")
        obj.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        """设置属性名称"""
        self.name = name

class Person:
    age = Validator(0,150)

    def __init__(self, name, age):
        self.name = name
        self.age = age   # 会调用Validator.__set__

# 使用示例
p = Person("Alice", 30)
print(p.age)
p.age = 200 # 会抛出ValueError
