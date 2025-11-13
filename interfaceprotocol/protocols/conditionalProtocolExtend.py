"""
条件协议拓展
"""
from typing import TypeVar, Protocol, Any, Union

T = TypeVar('T')


# 基础协议
class Serializer(Protocol):
    def serialize(self, obj: Any) -> str: ...


# 条件扩展
class TypedSerializer(Serializer, Protocol):
    def serialize_typed(self, obj: T) -> str: ...

    def deserialize_typed(self, data: str, target_type: type[T]) -> T: ...


# 多类型支持扩展
class MultiFormatSerializer(TypedSerializer, Protocol):
    def to_json(self, obj: Any) -> str: ...

    def to_xml(self, obj: Any) -> str: ...

    def from_json(self, data: str, target_type: type[T] = None) -> Union[T, dict]: ...

    def from_xml(self, data: str, target_type: type[T] = None) -> Union[T, dict]: ...