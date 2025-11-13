"""
装饰器模式拓展
"""
from typing import Protocol, Any, Callable


# 基础服务协议
class Service(Protocol):
    def execute(self, *args, **kwargs) -> Any: ...

# 拓展：支持中间件
class MiddlewareSupport(Service,Protocol):
    def add_middleware(self, middleware: Callable) -> None: ...

    def remove_middleware(self, middleware: Callable) -> None: ...


# 拓展: 支持生命周期钩子
class LifecycleService(MiddlewareSupport,Protocol):
    def on_start(self) -> None: ...

    def on_stop(self) -> None: ...

    def on_error(self, error: Exception) -> None: ...


# 实现
class BaseService:

    def __init__(self):
        self._middlewares = []

    def execute(self, *args, **kwargs) -> Any:
        # 基础执行逻辑
        result = self._execute_core(*args, **kwargs)
        return result

    def _execute_core(self, *args, **kwargs):
        raise NotImplementedError

    def add_middleware(self, middleware: Callable):
        self._middlewares.append(middleware)


    def remove_middleware(self, middleware: Callable):
        self._middlewares.remove(middleware)

    def on_start(self):
        print("Service starting...")

    def on_stop(self):
        print("Service stopping...")

    def on_error(self, error: Exception):
        print(f"Service error: {error}")
