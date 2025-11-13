"""
文件处理协议拓展
"""
from typing import Protocol, Iterator, ContextManager, Optional, runtime_checkable
import json
from pathlib import Path


# 基础文件读取协议 - 添加 runtime_checkable
@runtime_checkable
class FileReader(Protocol):
    def read_line(self) -> str: ...

    def read_lines(self) -> Iterator[str]: ...


# 扩展：支持不同格式 - 添加 runtime_checkable
@runtime_checkable
class JSONFileReader(FileReader, Protocol):
    def read_json(self) -> dict: ...

    def read_json_lines(self) -> Iterator[dict]: ...


# 扩展：支持上下文管理 - 添加 runtime_checkable
@runtime_checkable
class ContextualFileReader(JSONFileReader, ContextManager, Protocol):
    """支持上下文管理和JSON读取的文件阅读器"""
    pass


# 正确的实现类
class SmartFileHandler:
    def __init__(self, filename: str):
        self.filename = filename
        self._file = None

    def read_line(self) -> str:
        if self._file and not self._file.closed:
            line = self._file.readline()
            return line.strip() if line else ""
        raise IOError("File not open or closed")

    def read_lines(self) -> Iterator[str]:
        if self._file and not self._file.closed:
            self._file.seek(0)  # 回到文件开头
            for line in self._file:
                yield line.strip()
        else:
            raise IOError("File not open or closed")

    def read_json(self) -> dict:
        if self._file and not self._file.closed:
            self._file.seek(0)
            try:
                return json.load(self._file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON: {e}")
        raise IOError("File not open or closed")

    def read_json_lines(self) -> Iterator[dict]:
        if self._file and not self._file.closed:
            self._file.seek(0)
            for line_num, line in enumerate(self._file, 1):
                line = line.strip()
                if line:  # 跳过空行
                    try:
                        yield json.loads(line)
                    except json.JSONDecodeError as e:
                        print(f"Warning: Invalid JSON at line {line_num}: {e}")
                        continue
        else:
            raise IOError("File not open or closed")

    # 上下文管理器方法
    def __enter__(self):
        try:
            self._file = open(self.filename, 'r', encoding='utf-8')
            return self
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")
        except Exception as e:
            raise IOError(f"Failed to open file: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file and not self._file.closed:
            self._file.close()
        # 返回False让异常继续传播，返回True则抑制异常
        return False

    def is_open(self) -> bool:
        return self._file is not None and not self._file.closed

    def __repr__(self):
        status = "open" if self.is_open() else "closed"
        return f"SmartFileHandler(filename={self.filename}, status={status})"


# 创建测试数据
def create_test_files():
    """创建测试用的JSON文件"""
    # 普通JSON文件
    normal_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # JSON行文件
    lines_data = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False},
        {"id": 3, "name": "Charlie", "active": True}
    ]

    # 写入文件
    with open("test_data.json", "w", encoding='utf-8') as f:
        json.dump(normal_data, f, indent=2)

    with open("test_lines.jsonl", "w", encoding='utf-8') as f:
        for item in lines_data:
            f.write(json.dumps(item) + "\n")

    print("测试文件创建完成")


# 测试函数
def test_file_handler():
    """测试文件处理器"""
    print("=== 测试 SmartFileHandler ===")

    # 创建测试文件
    create_test_files()

    # 测试1: 普通JSON文件
    print("\n1. 测试普通JSON文件:")
    try:
        handler: ContextualFileReader = SmartFileHandler("test_data.json")
        with handler as f:
            print(f"文件状态: {f}")
            data = f.read_json()
            print(f"JSON数据: {data}")

            # 测试读取单行
            f._file.seek(0)  # 回到开头读取第一行
            first_line = f.read_line()
            print(f"第一行: {first_line}")

    except Exception as e:
        print(f"错误: {e}")

    # 测试2: JSON行文件
    print("\n2. 测试JSON行文件:")
    try:
        handler2 = SmartFileHandler("test_lines.jsonl")
        with handler2 as f:
            print(f"文件状态: {f}")

            print("所有JSON行:")
            for i, json_line in enumerate(f.read_json_lines(), 1):
                print(f"  行 {i}: {json_line}")

            print("所有文本行:")
            for i, text_line in enumerate(f.read_lines(), 1):
                print(f"  行 {i}: {text_line}")

    except Exception as e:
        print(f"错误: {e}")

    # 测试3: 错误处理
    print("\n3. 测试错误处理:")
    try:
        handler3 = SmartFileHandler("nonexistent_file.json")
        with handler3 as f:
            data = f.read_json()
    except FileNotFoundError as e:
        print(f"预期的文件未找到错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

    # 测试4: 协议检查 - 修复后的版本
    print("\n4. 测试协议兼容性:")

    # 创建新的实例进行测试
    handler_test = SmartFileHandler("test_data.json")

    # 检查是否满足各个协议 - 现在应该可以正常工作了
    print(f"是 FileReader: {isinstance(handler_test, FileReader)}")
    print(f"是 JSONFileReader: {isinstance(handler_test, JSONFileReader)}")
    print(f"是 ContextualFileReader: {isinstance(handler_test, ContextualFileReader)}")
    print(f"是 ContextManager: {isinstance(handler_test, ContextManager)}")

    # 检查具体的方法是否存在
    print(f"有 read_line 方法: {hasattr(handler_test, 'read_line')}")
    print(f"有 read_json 方法: {hasattr(handler_test, 'read_json')}")
    print(f"有 __enter__ 方法: {hasattr(handler_test, '__enter__')}")
    print(f"有 __exit__ 方法: {hasattr(handler_test, '__exit__')}")


# 更高级的扩展示例
@runtime_checkable
class AdvancedFileProtocol(ContextualFileReader, Protocol):
    """高级文件协议扩展"""

    def get_file_info(self) -> dict: ...

    def read_chunk(self, size: int) -> str: ...

    def seek(self, position: int) -> None: ...


class AdvancedFileHandler(SmartFileHandler):
    """扩展的文件处理器，添加更多功能"""

    def __init__(self, filename: str):
        super().__init__(filename)
        self._encoding = 'utf-8'

    def get_file_info(self) -> dict:
        """获取文件信息"""
        if self.is_open():
            return {
                "filename": self.filename,
                "encoding": self._encoding,
                "position": self._file.tell() if self._file else 0
            }
        return {"filename": self.filename, "status": "closed"}

    def read_chunk(self, size: int = 1024) -> str:
        """读取指定大小的块"""
        if self._file and not self._file.closed:
            return self._file.read(size)
        raise IOError("File not open")

    def seek(self, position: int) -> None:
        """移动文件指针"""
        if self._file and not self._file.closed:
            self._file.seek(position)
        else:
            raise IOError("File not open")


def test_advanced_handler():
    """测试高级文件处理器"""
    print("\n=== 测试 AdvancedFileHandler ===")

    try:
        advanced_handler = AdvancedFileHandler("test_data.json")

        # 测试协议兼容性
        print(f"是 AdvancedFileProtocol: {isinstance(advanced_handler, AdvancedFileProtocol)}")

        with advanced_handler as f:
            info = f.get_file_info()
            print(f"文件信息: {info}")

            # 读取前50个字符
            chunk = f.read_chunk(50)
            print(f"前50字符: {chunk}")

            # 回到开头
            f.seek(0)

    except Exception as e:
        print(f"错误: {e}")


def demonstrate_protocol_extension():
    """演示协议扩展的概念"""
    print("\n=== 协议扩展概念演示 ===")

    # 演示协议继承关系
    protocols = {
        'FileReader': ['read_line', 'read_lines'],
        'JSONFileReader': FileReader.__dict__.copy(),
        'ContextualFileReader': JSONFileReader.__dict__.copy(),
        'AdvancedFileProtocol': ContextualFileReader.__dict__.copy()
    }

    # JSONFileReader 添加的方法
    protocols['JSONFileReader'].update({'read_json', 'read_json_lines'})
    # ContextualFileReader 添加的方法（从 ContextManager）
    protocols['ContextualFileReader'].update({'__enter__', '__exit__'})
    # AdvancedFileProtocol 添加的方法
    protocols['AdvancedFileProtocol'].update({'get_file_info', 'read_chunk', 'seek'})

    print("协议扩展层次:")
    for protocol_name, methods in protocols.items():
        print(f"  {protocol_name}: {len(methods)} 个方法")
        if methods:
            method_list = [m for m in methods if not m.startswith('_')]
            if method_list:
                print(f"    主要方法: {', '.join(sorted(method_list)[:3])}...")


if __name__ == "__main__":
    # 运行测试
    test_file_handler()
    test_advanced_handler()
    demonstrate_protocol_extension()

    # 清理测试文件
    import os

    for file in ["test_data.json", "test_lines.jsonl"]:
        if os.path.exists(file):
            os.remove(file)
            print(f"\n已清理测试文件: {file}")