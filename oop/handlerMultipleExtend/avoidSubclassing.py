"""
避免子类化具体类
"""
from abc import ABC, abstractmethod


# 错误做法：子类化具体类
class BadHttpClient:
    """一个具体的 HTTP 客户端（不应该被继承）"""

    def __init__(self):
        self.timeout = 30

    def get(self, url):
        # 具体实现细节
        return f"GET {url} with timeout {self.timeout}"

    def post(self, url,data):
        # 具体实现细节
        return f"POST {url} with data {data}"

# 正确做法： 定义抽象接口
class HttpClient(ABC):
    """HTTP 客户端抽象接口"""

    @abstractmethod
    def get(self, url):
        pass

    @abstractmethod
    def post(self, url, data):
        pass

class RequestsHttpClient(HttpClient):
    """基于 requests 库的实现"""

    def get(self, url):
        # 实际使用requests 库
        return f"Requests GET: {url}"

    def post(self, url, data):
        return f"Requests POST: {url} with {data}"

class AsyncHttpClient(HttpClient):
    """异步 HTTP 客户端"""

    def get(self, url):
        return f"Async GET: {url}"

    def post(self, url, data):
        return f"Async POST: {url} with {data}"

# 装饰器模式拓展功能（而不是继承）
class RetryMixin:
    """重试功能混合类"""

    def __init__(self,max_retries=3):
        self.max_retries = max_retries

    def get_with_retry(self,url):
        for attempt in range(self.max_retries):
            try:
                return self.get(url)
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == self.max_retries - 1:
                    raise
        return None


class LoggingMixin:
    """日志记录混合类"""

    def get_with_logging(self,url):
        print(f"Making GET request to: {url}")
        result = self.get(url)
        print(f"Received response: {result}")
        return result


# 组合而不是继承
class EnhancedHttpClient:

    """增强的 HTTP 客户端（使用组合）"""

    def __init__(self, client: HttpClient):
        self.client = client
        self.retry = RetryMixin()
        # 将客户端的方法绑定到重试混合类
        self.retry.get = self.client.get

    def get(self,url):
        return self.retry.get_with_retry(url)

    def post(self,url,data):
        return self.client.post(url,data)

# 使用
basic_client = RequestsHttpClient()
enhanced_client = EnhancedHttpClient(basic_client)
print(enhanced_client.get("https://api.example.com/data"))
