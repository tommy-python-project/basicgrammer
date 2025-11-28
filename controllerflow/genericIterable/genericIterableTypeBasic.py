"""
泛化可迭代类型-演示
"""
from typing import Iterable, TypeVar, Callable


def basic_concepts():
    """泛化可迭代类型的基本概念"""

    print("=== 泛化可迭代类型 ===")

    # 传统方式： 具体的类型
    def process_strings(strings: list[str]) -> None:
        for s in strings:
            print(s.upper())

    # 泛化方式：任何可迭代的字符串
    def process_any_strings(strings: Iterable[str]) -> None:
        for s in strings:
            print(s.upper())

    # 测试不同的可迭代对象
    list_strings = ["hello","world"]
    tuple_strings = ("python","programming")
    set_strings = {"set","example"}

    print("列表:")
    process_any_strings(list_strings)

    print("\n元组:")
    process_any_strings(tuple_strings)

    print("\n集合:")
    process_any_strings(set_strings)

    # 甚至生成器
    def string_generator():
        yield "generator"
        yield "example"

    print("\n生成器:")
    process_any_strings(string_generator())

basic_concepts()


# 类型变量和泛型
from typing import TypeVar, Iterable
import itertools

"""类型变量与泛型"""
def type_variables_demo():
    """Python 3.13 版本的类型变量和泛型演示"""

    print("=== 类型变量和泛型 (Python 3.13) ===")

    # 定义类型变量
    T = TypeVar('T')  # 任意类型
    U = TypeVar('U')  # 另一个任意类型

    # 泛化函数：处理任何类型的可迭代对象
    def first_element(items: Iterable[T]) -> T | None:
        """返回可迭代对象的第一个元素"""
        for item in items:
            return item
        return None

    # 测试不同类型
    numbers = [1, 2, 3]
    words = ("hello", "world")
    empty = []

    print(f"第一个数字: {first_element(numbers)}")
    print(f"第一个单词: {first_element(words)}")
    print(f"空列表: {first_element(empty)}")

    # 更复杂的泛型函数 - 在 Python 3.13 中应该可以正常工作
    def transform_iterable(
            items: Iterable[T],
            transform_func: Callable[[T], U]
    ) -> list[U]:
        """转换可迭代对象中的每个元素"""
        return [transform_func(item) for item in items]

    # 应用转换
    squared = transform_iterable(numbers, lambda x: x ** 2)
    uppercased = transform_iterable(words, lambda x: x.upper())

    print(f"数字平方: {squared}")
    print(f"大写单词: {uppercased}")

type_variables_demo()