"""
实例方法 vs 静态方法 vs 类方法
"""

class MyClass:

    class_attribute = "类属性"

    def __init__(self,instance_value):
        self.instance_attribute = instance_value

    # 实例方法
    def instance_method(self):
        print(f"实例方法：实例属性={self.instance_attribute}，类属性={self.class_attribute}")
        return self.instance_attribute

    # 类方法
    @classmethod
    def class_method(cls):
        print(f"类方法：类属性={cls.class_attribute}")
        # print(self.instance_attribute)  # 错误！不能访问实例属性
        return cls.class_attribute

    # 静态方法
    @staticmethod
    def static_method():
        print("静态方法: 不能访问类属性或实例属性")
        return "静态方法返回值"


# 使用示例
obj = MyClass("实例值")

# 调用实例方法
print(obj.instance_method())  # 实例方法：实例属性 = 实例值，类属性 = 类属性值

# 调用类方法
print(MyClass.class_method())  # 类方法: 类属性=类属性值
print(obj.class_method())      # 也可以通过实例调用

# 调用静态方法
print(MyClass.static_method())  # 静态方法: 不能访问类属性或实例属性
print(obj.static_method())      # 也可以通过实例调用