"""
contextlib 工具 --- 提供了创建上下文管理器的便捷工具
"""
import io
import time
from contextlib import contextmanager, suppress, redirect_stdout


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"执行时间: {end - start:.2f}秒")

with timer():
    # 执行耗时操作
    sum(range(1000000))

# 2. 抑制特定异常
with suppress(FileNotFoundError):
    with open('不存在的文件.txt') as f:
        content = f.read()
    print("这行不会执行")
print("程序继续执行，没有崩溃")


# 3. 重定向输出
f = io.StringIO()
with redirect_stdout(f):
    print("这会被重定向")
print(f"捕获的输出: {f.getvalue()}")