"""
静态协议的核心作用
"""
import json
from abc import abstractmethod
from typing import Protocol, List, Iterator, TypeVar, runtime_checkable, Sequence, AsyncContextManager

"""
1. 实现鸭子类型的静态检查
"""

# 定义协议 - 管组“能做什么”而不是“是什么”
class SupportsRead(Protocol):
    def read(self,size : int = -1) -> bytes:
        ...

class SupportsWrite(Protocol):
    def write(self,data : bytes) -> int:
        ...


# 任何实现了read 方法的类都满足 SupportsRead 协议
class MyFile:
    def read(self,size : int = -1) -> bytes:
        return b'file content'

    # 不需要继承任何特定基类

class NetworkStream:
    def read(self, size: int = -1) -> bytes:
        return b"network data"

    def close(self) -> None:
        print("Closing connection")

# 使用协议作为类型提示
def read_data(source: SupportsRead) -> bytes:
    return source.read()

# 使用协议作为类型提示
def read_data(source: SupportsRead) -> bytes:
    return source.read()

# 所有实现了 read 方法 的对象都可以传入
file_obj = MyFile()
stream = NetworkStream()

data1 = read_data(file_obj)
data2 = read_data(stream)
print(data1)
print(data2)

"""
2. 解耦代码，减少依赖
"""

# 传统方法 - 依赖具体类
class DatabaseConnection:
    def execute_query(self, query: str) -> List[dict]:
        return [{"id": 1, "name": "Alice"}]

def process_database(conn: DatabaseConnection) -> None:
    # 紧密耦合到具体类
    result = conn.execute_query("select * from users")

# 使用协议 - 只依赖接口
class QueryExecutor(Protocol):
    def execute_query(self, query: str) -> List[dict]:
        ...

class MySQLConnection:
    def execute_query(self, query: str) -> List[dict]:
        print("Using MySQL")
        return [{"id": 1, "name": "Alice"}]

class PostgreSQLConnection:
    def execute_query(self, query: str) -> List[dict]:
        print("Using PostgreSQL")
        return [{"id": 1, "name": "Alice"}]

class MockConnection:
    def execute_query(self, query: str) -> List[dict]:
        print("Using mock data")
        return [{"id": 99, "name": "Test User"}]

def process_database_v2(executor: QueryExecutor)  -> None:
    # 可以接受任何实现了 execute_query 的对象
    result = executor.execute_query("SELECT * FROM users")
    print(result)

# 使用示例
mysql = MySQLConnection()
postgres = PostgreSQLConnection()
mock = MockConnection()

process_database_v2(mysql)
process_database_v2(postgres)
process_database_v2(mock)

"""
3. 支持现有代码的类型检查
"""

# 对现有代码添加类型检查，无需修改原有类
class SupportsIteration(Protocol):

    def __iter__(self) -> Iterator: ...

class CustomContainer:
    def __init__(self,data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    # 没有类型注解，但满足协议

def process_items(container: SupportsIteration) -> None:
    for item in container:
        print(item)

# 现有的类自动满足协议
my_container = CustomContainer([1, 2, 3])
process_items(my_container)


"""
4. 复杂的协议定义
"""

T = TypeVar('T')


# 更复杂的协议
class SupportsComparison(Protocol):
    @abstractmethod
    def __lt__(self, other) -> bool: ...

    @abstractmethod
    def __eq__(self, other) -> bool: ...


# 运行时检查支持
@runtime_checkable
class Serializable(Protocol):
    def to_json(self) -> str: ...

    @classmethod
    def from_json(cls, json_str: str): ...


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __lt__(self, other: 'Product') -> bool:
        return self.price < other.price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def to_json(self) -> str:
        return f'{{"name": "{self.name}", "price": {self.price}}}'

    # --- 添加这个缺失的方法 ---
    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)  # 真正的解析逻辑
        return cls(data['name'], data['price'])  # 'cls' 指向 Product 类


def sort_items(items: Sequence[SupportsComparison]) -> Sequence[SupportsComparison]:
    return sorted(items)


def export_to_json(obj: Serializable) -> str:
    return obj.to_json()


# 使用示例
products = [
    Product("Laptop", 999.99),
    Product("Mouse", 29.99),
    Product("Keyboard", 79.99)
]

# --- 现在再次检查 ---
p = Product("Laptop", 999.99)
print(f"p 实现了 Serializable 吗? {isinstance(p, Serializable)}")

sorted_products = sort_items(products)
json_data = export_to_json(products[0])

# 运行时检查
print(isinstance(products[0], Serializable))  # True


"""
实际应用场景
"""

# Web框架中的中间件协议
class Middleware(Protocol):

    async def process_request(self,request:dict) -> dict:
        ...

    async def process_response(self,response:dict) -> dict:
        ...

# 数据库连接池协议
class ConnectionPool(Protocol):
    def acquire(self) -> AsyncContextManager: ...
    def release(self, connection) -> None: ...


# 缓存后端协议
class CacheBackend(Protocol):
    def get(self, key: str) -> bytes: ...
    def set(self, key: str, value: bytes, timeout: int = None) -> None: ...
    def delete(self, key: str) -> bool: ...

# 具体的实现类
class RedisCache:
    def get(self, key: str) -> bytes:
        # Redis实现
        return b"redis_data"

    def set(self, key: str, value: bytes, timeout: int = None) -> None:
        print(f"Setting {key} in Redis")

    def delete(self, key: str) -> bool:
        return True

class MemoryCache: # <-- 正确：这是一个普通的类
    def get(self, key: str) -> bytes:
        # 内存实现
        return b"memory_data"

    def set(self, key: str, value: bytes, timeout: int = None) -> None:
        print(f"Setting {key} in memory")

    def delete(self, key: str) -> bool:
        return True

def use_cache(cache: CacheBackend, key: str) -> bytes:
    # 可以接受任何缓存实现
    data = cache.get(key)
    if not data:
        cache.set(key, b"new_data")
    return data

# 灵活使用不同的缓存实现
redis_cache = RedisCache()
memory_cache = MemoryCache()

data1 = use_cache(redis_cache, "user:1")
data2 = use_cache(memory_cache, "user:2")

print(data1)
print(data2)