"""
上下文管理器
"""

class MyContextManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"进入上下文: {self.name}")
        return self  # 返回的对象会被 as 关键字接收

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"退出上下文: {self.name}")
        # 如果返回 True，异常会被抑制
        return False

# 使用自定义上下文管理器
with MyContextManager("测试") as cm:
    print(f"正在使用: {cm.name}")
    # 这里可以执行操作