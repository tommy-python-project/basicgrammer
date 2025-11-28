"""
泛化可迭代类型 --实际项目应用
配置系统
"""
from typing import TypeVar, Protocol, Generic, Iterable


def configuration_system():
    """配置系统案例"""

    print("=== 配置系统案例 ===")

    T = TypeVar('T')

    class ConfigSource(Protocol):
        """配置源协议"""
        def get(self,key:str) -> T | None:
            ...

    class ConfigManager(Generic[T]):
        """通用配置管理器"""

        def __init__(self,source:Iterable[ConfigSource]):
            self.source= list(source)

        def get_value(self,key:str,default: T) -> T | None:
            """从多个源获取配置"""
            for source in self.source:
                value = source.get(key)
                if value is not None:
                    return value
                return default

        def get_all_values(self,key:str) -> Iterable[T] :
            """获取所有源中的值"""
            for source in self.source:
                value = source.get(key)
                if value is not None:
                    yield value


    # 实现不同的配置源
    class DictConfig:
        def __init__(self, data: dict):
            self.data = data

        def get(self, key: str) -> T | None:
            return self.data.get(key)

    class EnvConfig:
        def __init__(self, env_vars: dict):
            self.env_vars = env_vars

        def get(self, key: str) -> T | None:
            return self.env_vars.get(key.upper())



    # 使用示例
    dict_source = DictConfig({"host": "localhost", "port": 8080})
    env_source = EnvConfig({"HOST": "127.0.0.1", "TIMEOUT": "30"})

    config = ConfigManager([dict_source, env_source])

    print(f"Host: {config.get_value('host', 'unknown')}")
    print(f"Port: {config.get_value('port', 0)}")
    print(f"Timeout: {config.get_value('timeout', 10)}")

    print("所有host值:")
    for host in config.get_all_values('host'):
        print(f"  {host}")

configuration_system()

