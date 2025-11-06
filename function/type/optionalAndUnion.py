"""
optional 与 Union
Union[X, Y]: 表示一个值可以是类型 X 或类型 Y。
Optional[X]: 表示一个值可以是类型 X 或 None。它等同于 Union[X, None]。
"""
from typing import Optional, Union


# Optional 类型（等价于 Union[Type, None]）
def get_username(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "alice"
    return None

# Union类型
def process_value(value: Union[int,str,float]) -> str:
    return str(value)

# 使用示例
username = get_username(1) # 类型：Optional[str]
value1 = process_value(10) # 接受int
value2 = process_value("hello") # 接受str
print(username)
print(value1)
print(value2)
value3 = process_value(username)
print(value3)