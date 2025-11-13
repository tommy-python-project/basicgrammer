"""
子类化内置类型很棘手
"""
import collections

"""
1. dict字典演示
"""

# 1. 棘手的内置dict 子类
class BadDict(dict):
    def __setitem__(self, key, value):
        print(f"BadDict: setting {key} = {value}")
        super().__setitem__(key, value)


print("--- Testing BadDict (subclassing dict) ---")
# 场景 A: 使用 __init__ 初始化
bd = BadDict(a=1, b=2)
print("... __init__ 完成")

# 场景B：使用 update 方法
bd.update({'c':3,'d':4})
print("... update 完成")

# 场景C: 使用[] 赋值
bd['e'] = 5
print(f"Final BadDict: {bd}\n")

# 2. 正确的方式：UserDict
class GoodDict(collections.UserDict):
    def __setitem__(self, key, value):
        print(f"GoodDict: setting {key} = {value}")
        super().__setitem__(key, value)

print("--- Testing GoodDict (subclassing UserDict) ---")
# 场景A：使用__init__初始化
gd = GoodDict(a=1, b=2)
print("... __init__ 完成")

# 场景B ： 使用update 方法
gd.update({'c':3,'d':4})
print("... update 完成")

# 场景 C: 使用 [] 赋值
gd['e'] = 5
print(f"Final GoodDict: {gd}\n")


