"""
混合类的最佳实践
"""


class CacheMixin:
    """
    为类添加缓存功能的混合类
    要求使用类必须实现 _fetch_data 方法
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cache = {}

    def get_data(self, key):
        if key not in self._cache:
            self._cache[key] = self._fetch_data(key)
        return self._cache[key]

    def clear_cache(self):
        self._cache.clear()


class DataService(CacheMixin):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def _fetch_data(self, key):
        # 模拟从数据库获取数据
        return f"Data for {key} from database"


# 使用
service = DataService("db_connection")
print(service.get_data("user_1"))  # 从数据库获取
print(service.get_data("user_1"))  # 从缓存获取