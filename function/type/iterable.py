"""
Iterable 类型提示
"""
from typing import Iterable


# Iterable 类型提示
def process_items(items: Iterable[str]) -> str:
    return ", ".join(items)

# 返回迭代器
def number_generator(limit: int) -> Iterable[int]:
    for i in range(limit):
        yield i

# 使用示例
result = process_items(["apple", "banana", "cherry"])
print(result)
for num in number_generator(5):
    print(num)