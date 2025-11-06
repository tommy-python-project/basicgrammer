"""
带参数的装饰器
"""
import time


def retry(max_attempts = 3,delay = 1):
    def decorator(func):
        """重试装饰器"""
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    print(f"尝试 {attempts} 失败，{delay}秒后重试...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2)
def unreliable_operation():
    """模拟不可靠的操作"""
    import random
    if random.random() < 0.7:  # 70%的失败率
        raise ValueError("操作失败")
    return "操作成功"

# 测试
result = unreliable_operation()
print(result)
