"""
条件类型注解
"""
from typing import TypeVar, Any, Sequence, Union, overload

T = TypeVar('T')

def first_item(data: T) -> Any:
    """获取第一个元素，针对序列类型"""
    if hasattr(data, '__getitem__') and hasattr(data, '__len__'):
        if len(data) > 0:  # type: ignore
            return data[0]  # type: ignore
    return None

# 使用 overload 提供更好的类型信息

@overload
def safe_first(data: Sequence[T]) -> Union[T, None]: ...

@overload
def safe_first(data: T) -> Union[T, None]: ...

def safe_first(data: Any) -> Union[T, None]:
    if isinstance(data, Sequence) and not isinstance(data, str):
        return data[0] if data else None
    return data