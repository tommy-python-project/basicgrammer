"""
any类型
"""
from typing import Any


def flexible_function(data: Any) -> Any:
    # 可以接受任何类型，返回任何类型
    return data

# 使用示例
result1 = flexible_function("hello")
result2 = flexible_function(2)
result3 = flexible_function([1,2,3])
print(result1)
print(result2)
print(result3)