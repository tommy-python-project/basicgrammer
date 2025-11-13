"""
泛型协议拓展
"""
from typing import TypeVar, Protocol, Generic, Optional, List

T = TypeVar('T')
K = TypeVar('K')

# 基础泛型仓库协议
class GenericRepository(Protocol, Generic[T,K]):
    def get(self,id: K) -> Optional[T]: ...

    def get_all(self) -> List[T]: ...


# 拓展泛型协议
class SearchableRepository(GenericRepository[T,K],Protocol,Generic[T,K]):
    def search(self,query: str) -> List[T]: ...

    def filter(self, **criteria) -> List[T]: ...

# 进一步拓展
class PaginatedRepository(SearchableRepository[T, K], Protocol, Generic[T, K]):
    def get_page(self, page: int, page_size: int) -> List[T]: ...

    def get_total_pages(self, page_size: int) -> int: ...

# 具体实现
class UserRepository(PaginatedRepository['User',int]):
    def get(self, id: int) -> Optional['User']:
        # 实现具体逻辑
        pass

    def get_all(self) -> List['User']:
        pass

    def search(self, query: str) -> List['User']:
        pass

    def filter(self, **criteria) -> List['User']:
        pass

    def get_page(self, page: int, page_size: int) -> List['User']:
        pass

    def get_total_pages(self, page_size: int) -> int:
        pass

class User:
    pass

