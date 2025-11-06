"""
抽象基类
"""
from abc import ABC, abstractmethod
from typing import Iterable, Mapping, List, Sequence

import sequence


# 1. 定义“合同”（ABC）
class FileParser(ABC):

    @abstractmethod
    def load_data(self,path:str):
        """从路径加载数据"""
        pass

    @abstractmethod
    def parse(self) -> dict:
        """解析数据并返回字典"""
        pass


# 2. 尝试实例化 ABC -> 会失败
# parser = FileParser()
# TypeError: Can't instantiate abstract class FileParser without an implementation for abstract methods 'load_data', 'parse'

# 3. 签署“合同”（具体实现）
class JsonParser(FileParser):
    def __init__(self):
        self._data = None

    def load_data(self,path:str):
        print(f"从 {path} 加载 JSON")
        self._data = "{...}"  # 实际的加载逻辑

    def parse(self) -> dict:
        print("解析 JSON")
        return {"data": "json_data"}

# 4. 尝试“签署”一个不完整的合同 --> 同样会失败！
class BadXmlParser(FileParser):
    def load_data(self,path:str):
        print(f"从 {path} 加载 XML")
        # 糟糕！忘记实现 parse() 方法了

# xml_parser = BadXmlParser()
# TypeError: Can't instantiate abstract class BadXmlParser without an implementation for abstract method 'parse'

# 5. 正确实例化：
json_parser = JsonParser()
json_parser.load_data("file.json")


# 接受任何可迭代对象（list,tuple、set、generator）
def print_items(items: Iterable[int]):
    for item in items:
        print(item)

# 接受任何序列（list,tuple,str）,支持索引和切片
def get_first(seq: Sequence[str]) -> str:
    return seq[0]

# 接受任何只读映射（dict,defaultdict）
def print_keys(m: Mapping[str,int]):
    for key in m :
        print(key)


numbers: List[int] = [1, 2, 3]
print_items(numbers)

print(get_first(numbers))

regular_dict: dict[str, int] = {'Alice':100,'Bob':90}
print_keys(regular_dict)