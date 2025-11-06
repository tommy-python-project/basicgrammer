"""
属性访问类型的魔术方法
"""

class AttributeManager:

    def __init__(self):
        self.data = {}

    def __getattr__(self, name):
        """访问不存在的属性时调用"""
        print(f"Getting undefined attribute : {name}")
        return self.data.get(name, None)

    def __setattr__(self, name, value):
        """设置属性时调用"""
        if name == "data":
            super().__setattr__(name, value)
        else:
            print(f"Setting {name} = {value}")
            self.data[name] = value

    def __delattr__(self, name):
        """删除属性时调用"""
        print(f"Deleting {name}")
        del self.data[name]

    def __getattribute__(self, name):
        """访问任何属性时都会调用（优先级最高）"""
        # 注意：要避免无限递归
        return super().__getattribute__(name)

# 使用示例
obj = AttributeManager()
obj.name = "test"
print(obj.name)
print(obj.undefined)
