"""
用显示混合类实现代码复用
"""
import json
import pickle
from datetime import datetime


# 明确的混合类
class TimestampMixin:
    """时间戳功能混合类"""

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_timestamp(self):
        self.updated_at = datetime.now()


class JSONSerializationMixin:
    """JSON 序列化混合类"""

    def to_json(self, indent=2):
        data = self.to_dict() if hasattr(self, 'to_dict') else self.__dict__
        return json.dumps(data, indent=indent, default=str)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)


class PickleSerializationMixin:
    """Pickle 序列化混合类"""

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)


class ValidationMixin:
    """验证功能混合类"""

    def validate_required_fields(self, required_fields):
        missing = [field for field in required_fields
                  if not hasattr(self, field) or getattr(self, field) is None]
        if missing:
            raise ValueError(f"Missing required fields: {missing}")
        return True


# 使用混合类构建业务类
class User(TimestampMixin, JSONSerializationMixin, ValidationMixin):

    def __init__(self, username, email, age=None):
        super().__init__()
        self.username = username
        self.email = email
        self.age = age

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'age': self.age,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def save(self):
        self.validate_required_fields(['username', 'email'])
        self.update_timestamp()
        print(f"User {self.username} saved")

# 使用
user = User("john_doe", "john@example.com", 30)
user.save()

# 序列化功能
json_data = user.to_json()
print("JSON:", json_data)

