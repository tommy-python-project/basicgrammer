"""
1. 对象的创建与销毁
"""

class MyClass:

    def __new__(cls,*args,**kwargs):
        """创建实例（在__init__之前调用）"""
        print("Creating instance")
        instance = super().__new__(cls)
        return instance

    def __init__(self,name):
        """初始化实例"""
        print(f"Initializing with name : {name}")
        self.name = name

    def __del__(self):
        """对象被垃圾回收时调用"""
        print(f"Destroying {self.name}")


# 使用示例
obj = MyClass("test")
del obj