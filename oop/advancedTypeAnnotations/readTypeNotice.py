"""
运行时读取类型提示
"""
from typing import List, get_type_hints, get_origin, get_args, Union, Optional, Dict


class DataProcessor:

    def __init__(self, data: List[int]) -> None:
        self.data = data

    def process(self,multiplier: float) -> List[float]:
        return [x * multiplier for x in self.data]


# 获取类型提示
type_hints = get_type_hints(DataProcessor.__init__)
print(f"__init__ 类型提示: {type_hints}")

method_hints = get_type_hints(DataProcessor.process)
print(f"process 方法类型提示: {method_hints}")

# 解析复杂类型
def analyze_type(t: type) -> None:
    origin = get_origin(t)
    args = get_args(t)
    print(f"类型: {t}")
    print(f"原始类型: {origin}")
    print(f"类型参数: {args}")


# 分析复杂类型
complex_type = Dict[str,List[Optional[Union[int,str]]]]
analyze_type(complex_type)