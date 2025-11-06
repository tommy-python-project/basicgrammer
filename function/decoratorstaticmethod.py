"""
内置装饰器
@staticmethod 和 @classmethod
"""

class MyClass:
    class_var = "类变量"

    @staticmethod
    def static_method():
        print("静态方法，不需要实例或类")

    @classmethod
    def class_method(cls):
        print(f"类方法，可以访问类：{cls.class_var}")
        
    def instance_method(self):
        print("实例方法")

MyClass.static_method()
MyClass.class_method()