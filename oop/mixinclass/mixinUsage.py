"""
混合类实际应用
"""
from abc import ABC, abstractmethod
from datetime import datetime

from oop.mixinclass.jsonMixin import SerializableMixin


class DatabaseModel(ABC):
    """抽象基类"""
    @abstractmethod
    def save(self):
        pass


class TimestampMixin:
    """时间戳混合类"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_timestamp(self):
        self.updated_at = datetime.now()

class AuditMixin:
    """审计混合类"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.created_by = "system"

    def set_creator(self,user):
        self.created_by = user

class User(TimestampMixin, AuditMixin, DatabaseModel):
    def __init__(self,username,email):
        # 注意： 多重继承时，要确保所有父类的__init__都被正确调用
        super().__init__()
        self.username = username
        self.email = email

    def save(self):
        self.update_timestamp()
        print(f"Saving user: {self.username}")
        # 实际的保存逻辑...

# 使用
user = User("john_doe", "john@example.com")
user.set_creator("admin")
user.save()
print(f"Created at: {user.created_at}")
print(f"Created by: {user.created_by}")