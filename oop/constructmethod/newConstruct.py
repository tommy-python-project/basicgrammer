"""
__new__方法（对象创建）
"""

class Singleton:

    """单例模式：确保类只有一个实例"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        _new__ 在__init__之前调用，用于创建对象
        """
        print("调用__new__方法")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self,value):
        print("调用__init__方法")
        self.value = value


# 使用示例
s1 = Singleton(10)
s2 = Singleton(20)

print(s1 is s2)
print(s1.value)
print(s2.value)