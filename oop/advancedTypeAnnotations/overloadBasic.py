"""重载签名基础"""
from typing import overload, Union, TypeVar, Any, Sequence, Optional

"""重载签名基础"""

@overload
def proces_data(data: int) -> str: ...

@overload
def process_data(data: str) -> int: ...

@overload
def process_data(data: list[int]) -> list[str]: ...

def process_data(data: Union[int, str,list[int]]) -> Union[int, str,list[str]]:
    if isinstance(data, int):
        return f"Number: {data}"
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, list):
        return [str(x) for x in data]
    else:
        raise TypeError("Unsupported type")

# 使用示例
result1: str = process_data(42) # 类型检查器知道返回 str
result2: int = process_data("hello")  # 类型检查器知道返回 int
result3: list[str] = process_data([1, 2, 3])  # 类型检查器知道返回 list[str]
print(result1)
print(result2)
print(result3)

"""
重载max函数
"""


class Comparable:
    def __lt__(self, other: Any) -> bool: ...


T = TypeVar('T', bound=Comparable)


@overload
def my_max(_arg1: T, arg2: T) -> T: ...

@overload
def my_max(__arg1: T, __arg2: T, *args: T) -> T: ...

@overload
def my_max(__iterable: Sequence[T]) -> T: ...

def my_max(first: Union[T, Sequence[T]],
          second: Optional[T] = None,
          *args: T) -> T:
    if second is None:
        # 单参数版本 - 处理可迭代对象
        if not first:
            raise ValueError("max() arg is an empty sequence")
        if hasattr(first, '__iter__') and not isinstance(first, str):
            return max(first)  # type: ignore
        else:
            raise TypeError("Expected a sequence")
    elif not args:
        # 双参数版本
        return first if first >= second else second  # type: ignore
    else:
        # 多参数版本
        all_args = (first, second) + args
        return max(all_args)  # type: ignore

# 使用示例
print(my_max(1, 2))
print(my_max(1, 2, 3, 4))
print(my_max([1, 2, 3, 4]))



