"""
插件系统
"""
from typing import TypeVar, Protocol, Generic, Iterable


def plugin_system():

    """插件系统案例"""

    print("\n=== 插件系统案例 ===")

    T = TypeVar('T')

    class Plugin(Protocol):
        """插件协议"""
        def process(self,data: T) -> T:
            ...

    class PluginPipline(Generic[T]):


        def __init__(self,plugins:Iterable[Plugin]):
            self.plugins = list(plugins)

        def process_data(self,data: T) -> T:
            """通过所有插件处理数据"""
            result = data
            for plugin in self.plugins:
                result = plugin.process(result)
            return result

        def add_plugin(self,plugin: Plugin) -> None:
            """添加插件"""
            self.plugins.append(plugin)


    # 实现具体插件
    class UpperCasePlugin:
        def process(self,data: str) -> str:
            return data.upper()

    class ExclamationPlugin:
        def process(self,data: str) -> str:
            return data + "!"

    class ReversePlugin:
        def process(self,data: str) -> str:
            return data[::-1]


    # 使用示例
    plugins = [UpperCasePlugin(),ReversePlugin(),ExclamationPlugin()]
    pipeline = PluginPipline[str](plugins)

    result = pipeline.process_data("hello world")
    print(f"插件处理结果: {result}")

plugin_system()

