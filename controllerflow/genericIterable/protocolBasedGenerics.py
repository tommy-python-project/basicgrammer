"""
协议和结构化类型
"""
from typing import Protocol, runtime_checkable, Iterable


def protocol_based_generics():
    """基于协议的泛型"""

    print("\n=== 基于协议的泛型 ===")

    @runtime_checkable
    class Sized(Protocol):
        """有大小协议"""
        def __len__(self) -> int: ...

    @runtime_checkable
    class Addable(Protocol):
        """可相加协议"""
        def __add__(self, other) -> 'Addable': ...

    def process_sized_items(items: Iterable[Sized]) -> list[int]:
        """处理有大小属性的对象"""
        return [len(item) for item in items]

    def sum_addable(items: Iterable[Addable], start: Addable) -> Addable:
        """求和可相加对象"""
        result = start
        for item in items:
            result = result + item
        return result


    # 测试
    string_list = ["hello", "world", "python"]
    list_list = [[1, 2], [3, 4, 5], [6]]

    print(f"字符串长度: {process_sized_items(string_list)}")
    print(f"列表长度: {process_sized_items(list_list)}")

    numbers = [1, 2, 3, 4, 5]
    strings = ["a", "b", "c"]

    print(f"数字求和: {sum_addable(numbers, 0)}")
    print(f"字符串连接: {sum_addable(strings, '')}")


protocol_based_generics()


