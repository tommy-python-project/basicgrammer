"""
类型校正（Type Casting）
"""
import json
from typing import List, cast, Dict, Any, TypeGuard


def find_first_string(items: List[object]) -> str:
    for item in items:
        if isinstance(item, str):
            return item
        return "Default"


# 假设我们在某处获得了一个对象，我们十分确定它是 int，但编译器不知道
value: object = 10
# 强制转换为 int 以便通过检查
count = cast(int,value)
print(count + 5)


def parse_json_data(json_str: str) -> Dict[str, Any]:
    data = json.loads(json_str)
    # 我们知道返回的是 Dict[str,Any],但json.loads 返回 Any
    return cast(Dict[str, Any], data)

# 更安全的类型校正方式
def safe_cast(typ: type,obj: Any) -> Any:
    """运行时类型检查的cast"""
    if not isinstance(obj, typ):
        raise TypeError(f"Expected {typ}, got {type(obj)}")
    return obj

# 使用 isinstance 进行类型收窄
def process_value(value: Any) -> str:
    if isinstance(value, str):
        # 这里 value 被收窄为 str
        return value.upper()
    elif isinstance(value, int):
        # 这里 value 被收窄为 int
        return str(value * 2)
    else:
        return "unknown"


# 使用 TypeGuard
def is_string_list(val: List[Any]) -> TypeGuard[List[str]]:
    return all(isinstance(x,str) for x in val)

def process_strings(data: List[Any]) -> None:
    if is_string_list(data):
        # 这里data 被收窄为 List[str]
        for s in data:
            print(s.upper())  # 类型安全！
