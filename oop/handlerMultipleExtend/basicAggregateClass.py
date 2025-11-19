"""
聚合类简化了常见用例的创建。
"""


# 基础混合类
class CRUDMixin:
    """CRUD 操作混合类"""

    def create(self, data):
        print(f"Creating record with data: {data}")
        return 1  # 返回 ID

    def read(self, id):
        print(f"Reading record {id}")
        return {"id": id, "data": "sample"}

    def update(self, id, data):
        print(f"Updating record {id} with data: {data}")
        return True

    def delete(self, id):
        print(f"Deleting record {id}")
        return True


class CacheMixin:
    """缓存功能混合类"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cache = {}

    def get_cached(self, key):
        return self._cache.get(key)

    def set_cached(self, key, value):
        self._cache[key] = value


class LoggingMixin:
    """日志记录混合类"""

    def log_operation(self, operation, details):
        print(f"[{self.__class__.__name__}] {operation}: {details}")


# 聚合类：为常见用例提供预配置组合
class SimpleRepository(CRUDMixin, LoggingMixin):
    """简单仓储聚合类"""

    def create(self, data):
        self.log_operation("CREATE", data)
        return super().create(data)

    def read(self, id):
        self.log_operation("READ", id)
        return super().read(id)


class CachedRepository(CRUDMixin, CacheMixin, LoggingMixin):
    """带缓存的仓储聚合类"""

    def read(self, id):
        # 先尝试从缓存获取
        cached = self.get_cached(id)
        if cached:
            self.log_operation("READ_CACHED", id)
            return cached

        # 缓存未命中，从数据源读取
        result = super().read(id)
        self.set_cached(id, result)
        self.log_operation("READ_NEW", id)
        return result


# 专门化的聚合类
class UserRepository(CachedRepository):
    """用户专用的仓储类"""

    def get_by_username(self, username):
        # 模拟根据用户名查询
        return self.read(f"user_{username}")


class ProductRepository(SimpleRepository):
    """产品专用的仓储类"""

    def get_products_by_category(self, category):
        # 模拟根据分类查询
        return [self.read(f"product_{category}_{i}") for i in range(3)]


# 使用聚合类
user_repo = UserRepository()
product_repo = ProductRepository()

# 用户操作
user_id = user_repo.create({"username": "alice", "email": "alice@example.com"})
user_data = user_repo.read(user_id)  # 第一次读取，会缓存
user_data_cached = user_repo.read(user_id)  # 第二次读取，从缓存获取

# 产品操作
product_repo.create({"name": "Laptop", "price": 999})
products = product_repo.get_products_by_category("electronics")