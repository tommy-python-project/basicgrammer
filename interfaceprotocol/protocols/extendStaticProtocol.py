"""
拓展一个协议
"""
from typing import Protocol, runtime_checkable, List, Optional


@runtime_checkable
class BaseReader(Protocol):
    def read(self) -> str: ...

@runtime_checkable
class AdvancedReader(BaseReader, Protocol):
    def read_line(self) -> str: ...
    def seek(self,position: int) -> None: ...

class FileReader:
    def read(self) -> str:
        return "File content"

    def read_line(self) -> str:
        return "Line content"

    def seek(self, position: int) -> None:
        print(f"Seeking to {position}")


reader = FileReader()
print(isinstance(reader, AdvancedReader))


"""
拓展协议的多种方式

1- 垂直拓展（添加新方法）
"""

# 基础数据访问协议
class DataReader(Protocol):
    def read_record(self, id: int) -> dict: ...

    def get_total_count(self) -> int: ...

# 拓展：添加批量操作
class BatchDataReader(DataReader, Protocol):
    def read_batch(self, ids: List[int]) -> List[dict]: ...

    def read_all(self) -> List[dict]: ...

# 进一步拓展： 添加过滤功能
class FilterableDataReader(BatchDataReader, Protocol):
    def read_with_filter(self, **filters) -> List[dict]: ...

    def get_filtered_count(self, **filters) -> int: ...


"""
2-水平拓展（添加可选功能）
"""

# 核心协议
class Cache(Protocol):

    def get(self,key: str) -> Optional[bytes]: ...

    def set(self,key: str,value: bytes) -> None: ...

# 拓展协议A：添加过期功能
class ExpirableCache(Cache, Protocol):
    def set_with_ttl(self,key: str,value: bytes,ttl:int) -> None: ...

    def get_remaining_ttl(self,key: str) -> Optional[int]: ...


# 拓展协议B：添加统计功能
class MonitoredCache(Cache, Protocol):
    def get_hit_count(self) -> int: ...

    def get_miss_count(self) -> int: ...

    def get_stats(self) -> dict: ...


# 组合拓展
class AdvancedCache(ExpirableCache,MonitoredCache, Protocol):
    """结合了过期和监控功能的缓存"""
    def clear_expired(self) -> None: ...



