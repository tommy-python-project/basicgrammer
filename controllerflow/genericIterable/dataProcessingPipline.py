"""
泛化可迭代类型的实际应用
"""
from typing import TypeVar, Generic, Callable, List, Iterable


# 1. 数据处理管道
def data_processing_pipline():
    """数据处理管道应用"""

    print("=== 数据处理管道 ===")

    T = TypeVar('T')
    U = TypeVar('U')

    class DataPipeline(Generic[T,U]):
        """通用的数据处理管道"""

        def __init__(self):
            self.operations: List[Callable] = []

        def map(self,func: Callable[[T],U]) -> 'DataPipeline[T,U]':
            """添加映射操作"""
            self.operations.append(('map', func))
            return self

        def filter(self,func: Callable[[T],bool]) -> 'DataPipeline[T,T]':
            """添加过滤操作"""
            self.operations.append(('filter', func))
            return self

        def process(self,data: Iterable[T]) -> Iterable[U]:
            """处理数据"""
            result: Iterable = data

            for op_type,func in self.operations:
                if op_type=='map':
                    result = (func(item) for item in result)
                elif op_type=='filter':
                    result = (item for item in result if func(item))

            yield from result


    # 使用示例
    pipeline = (DataPipeline[int,int]()
                .filter(lambda x: x % 2 == 0) # 只保留偶数
                .map(lambda x: x ** 2)        # 平方
                .map(lambda x: x + 10)        # 加10
                )

    numbers = [1,2,3,4,5,6,7,8,9,10]
    result = list(pipeline.process(numbers))

    print(f"原始数据: {numbers}")
    print(f"处理结果: {result}")

data_processing_pipline()

