"""
字符串表示
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """用户友好的字符串表示"""
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        """开发者友好的字符串表示，应该能重建对象"""
        return f"Person('{self.name}', {self.age})"

    def __format__(self,format_spec):
        """自定义格式化"""
        if format_spec == "short":
            return self.name
        elif format_spec == "full":
            return f"{self.name} ({self.age})"
        return str(self)


# 使用示例
p = Person("Alice",30)
print(str(p))
print(repr(p))
print(f"{p:short}")
print(f"{p:full}")


