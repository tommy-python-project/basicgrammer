"""
__del__析构方法
"""

class FileHandler:

    def __init__(self, filename):
        """打开文件"""
        self.filename = filename
        print(f"打开文件：{filename}")

    def __del__(self):
        """
        析构方法：对象被销毁时自动调用
        用于清理资源（如关闭文件、释放连接等）
        """
        print(f"关闭文件：{self.filename}")
        # 执行清理工作

# 使用示例
file = FileHandler("test.txt")
print("正在处理文件...")
del file #手动删除对象，触发__del__
print("文件处理完成")

# 或者自动销毁（作用域结束时）
def process_file():
    file = FileHandler("test.txt")
    print("函数内处理文件")
    # 函数结束时，file被销毁，自动调用__del__


process_file()