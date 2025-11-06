"""
可调用对象
"""
class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self,value):
        """使对象可调用：obj(args)"""
        return value * self.factor

# 使用示例
double = Multiplier(2)
triple = Multiplier(3)
print(double(5))
print(triple(5))

