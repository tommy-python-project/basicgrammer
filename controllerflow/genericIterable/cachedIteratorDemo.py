"""
通用缓存迭代器
"""
from typing import TypeVar, Generic, Iterable, List, Iterator


def cached_iterator_demo():
    """通用缓存迭代器"""

    print("\n=== 通用缓存迭代器 ===")

    T = TypeVar("T")

    class CachedIterator(Generic[T]):
        """可多次迭代的缓存迭代器"""

        def __init__(self,iterable: Iterable[T]):
            self.iterable = iter(iterable)
            self.cache: List[T] = []
            self.exhausted = False


        def __iter__(self) -> Iterator[T]:
            """支持多次迭代"""
            # 首先产生缓存的内容
            yield from self.cache

            # 如果迭代器未耗尽，继续迭代
            if not self.exhausted:
                for item in self.iterable:
                    self.cache.append(item)
                    yield item
                self.exhausted = True


        def __next__(self) -> T:
            """手动迭代"""
            try:
                item = next(self.iterable)
                self.cache.append(item)
                return item
            except StopIteration:
                self.exhausted = True
                raise


    # 测试缓存迭代器
    def expensive_generator():
        """模拟昂贵的生成器"""
        for i in range(5):
            print(f"生成值: {i}")
            yield i

    print("第一次迭代:")
    cached = CachedIterator(expensive_generator())
    first_pass = list(cached)
    print(f"第一次结果: {first_pass}")


    print("\n第二次迭代（使用缓存）:")
    second_pass = list(cached)
    print(f"第二次结果: {second_pass}")

cached_iterator_demo()


