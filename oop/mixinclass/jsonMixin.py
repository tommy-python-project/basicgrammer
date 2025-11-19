"""
时间戳与Json序列化 mixin
"""
# mixins.py
class LoggingMixin:
    """日志记录的混合类"""
    def log(self,message):
        print(f"[{self.__class__.__name__}] {message}]")

class SerializableMixin:
    """序列化混合类"""
    def to_dict(self):
        return {
            key: value for key, value in self.__dict__.items() if not key.startswith('_')
        }

class MyClass(LoggingMixin, SerializableMixin):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def process(self):
        self.log(f"Processing {self.name}")  # 来自 LoggingMixin
        return self.value * 2

# 使用
obj = MyClass('test', 10)
obj.process()  # 输出: [MyClass] Processing test
print(obj.to_dict())  # 输出: {'name': 'test', 'value': 10}
