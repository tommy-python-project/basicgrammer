"""
静态协议
"""
from typing import Protocol


class SupportsRead(Protocol):
    def read(self) -> str: ...

def process_readable(obj: SupportsRead) -> str:
    return obj.read()