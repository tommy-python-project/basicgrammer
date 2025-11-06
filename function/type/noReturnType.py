"""
NoReturn 是一个特殊的类型，用于注解永不返回的函数
"""
from typing import NoReturn


# 函数不会返回的情况
def raise_error(message: str) -> NoReturn:
    raise ValueError(message)

def exit_program() -> NoReturn:
    print("Exiting program...")
    exit(0)

try:
    raise_error("Something went wrong")
except ValueError as e:
    print(f"Caught error: {e}")

exit_program()