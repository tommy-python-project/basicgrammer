"""
TypedDict (结构化字典)
"""
from typing import TypedDict, Optional, List, NotRequired, Any


class Person(TypedDict):
    name: str
    age: int
    email: Optional[str]
    hobbies: List[str]

# 创建 TypedDict实例
person1: Person = {
    "name": "Alice",
    "age": 22,
    "email": "alice@example.com",
    "hobbies": ["reading", "swimming"],
}

# 部分初始化（需要设置 total=False）
class PartialPerson(TypedDict,total=False):
    name: str
    age: int
    email: str

person2: PartialPerson = {"name":"Bob"}

# 使用示例
def process_person(person: Person) -> str:
    return f"{person['name']} is {person['age']} years old"

# 类型检查会捕获错误
# person1["invalid_key"] = "value"


"""
继承和混合使用
"""

class BaseUser(TypedDict):
    username: str
    created_at: str

class UserProfile(BaseUser):
    email: NotRequired[str] # 可选字段
    age: NotRequired[int]
    preferences: dict[str,Any]

# 创建实例
profile : UserProfile = {
    "username": "john_doe",
    "created_at": "2023-01-01",
    "preferences": {"theme": "dark"}
}