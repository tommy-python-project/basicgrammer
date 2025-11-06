"""
装饰器模式
函数装饰器
"""
import time


# 装饰器函数
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        # 核心：调用被装饰的原函数（原组件）
        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time

        # 装饰器添加的额外职责（新功能）
        print(f"函数 {func.__name__} 执行耗时: {duration:.4f} 秒")
        return result

    return wrapper

# 使用装饰器
@log_execution_time
def complex_calculation(n):
    total = 0
    for i in range(n):
        total += i
    return total

# 调用时，实际上调用的是 wrapper 函数
result = complex_calculation(100000)
print(f"结果: {result}")