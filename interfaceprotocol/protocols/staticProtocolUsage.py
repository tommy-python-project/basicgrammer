"""
静态协议设计最佳实践
"""
from typing import Protocol, runtime_checkable



# 协议应该小而专注

@runtime_checkable
class Readable(Protocol):
    def read(self,size : int = -1) -> bytes: ...

@runtime_checkable
class Writable(Protocol):
    def write(self,data : bytes): ...


@runtime_checkable
class ReadWrite(Readable, Writable, Protocol):
    """组合协议"""
    def close(self) -> None: ...

class SimpleIO:
    def read(self,size : int = -1) -> bytes:
        return b"data"

    def write(self,data : bytes):
        return len(data)

    def close(self) -> None:
        print("Closed")

simple_io = SimpleIO()
print(isinstance(simple_io, ReadWrite))
