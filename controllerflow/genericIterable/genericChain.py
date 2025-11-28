"""
重新实现chain
"""
import itertools
from typing import Iterable, TypeVar, Callable


# 基础chain实现
def custom_chain_implementation():
    """自定义 chain实现"""

    print("=== 重新实现 itertools.chain ===")

    T = TypeVar('T')  # 任意类型

    def my_chain(*iterables: Iterable[T])  -> Iterable[T]:
        """自定义 chain 实现"""
        for iterable in iterables:
            yield from iterable


    # 测试自定义 chain
    list1 = [1, 2, 3]
    tuple1 = (4,5,6)
    set1 = {7,8,9}

    result = list(my_chain(list1, tuple1, set1))
    print(f"自定义 chain 结果: {result}")

    # 与标准库比较
    std_result = list(itertools.chain(list1, tuple1, set1))
    print(f"标准 chain 结果: {std_result}")
    print(f"结果相同: {result == std_result}")

custom_chain_implementation()

def enhanced_chain():
    """增强版 chain 实现"""
    print("\n=== 增强版 chain ===")

    T = TypeVar('T')  # 任意类型

    def smart_chain(
            *iterables: Iterable[T],
            filter_func: Callable[[T], bool] | None = None,
            transform_func: Callable[[T], T] | None = None
    ) -> Iterable[T]:
        """
        增强的 chain 实现，支持过滤和转换
        :param iterables:  多个迭代对象
        :param filter_func:  可选的过滤函数
        :param transform_func: 可选的转换函数
        :return:
        """
        for iterable in iterables:
            for item in iterable:
                # 应用过滤
                if filter_func and not filter_func(item):
                    continue
                # 应用转换
                if transform_func:
                    yield transform_func(item)
                else:
                    yield item

    # 测试增强功能
    numbers1 = [1, 2, 3,4,5]
    numbers2 = [6,7,8,9,10]

    # 只连接够数并平方
    result = list(smart_chain(
        numbers1, numbers2,
        filter_func=lambda n: n % 2 == 0,
        transform_func=lambda x: x ** 2
    ))

    print(f"过滤偶数并平方: {result}")

enhanced_chain()