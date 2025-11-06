"""
上下文管理器的魔术方法
"""
class FileManager:

    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """进入with语句时调用"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出with语句时调用"""
        print(f"Closing {self.filename}")
        if self.file :
            self.file.close()
        # 返回False 表示不抑制异常
        return False

# 使用示例
with FileManager("test.txt","w") as file:
    file.write("hello world")
# 自动调用__exit__关闭文件