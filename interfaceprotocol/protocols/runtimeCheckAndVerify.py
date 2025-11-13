"""
运行时检查与验证
"""
from typing import Protocol, runtime_checkable


@runtime_checkable
class BasicAuth(Protocol):
    def login(self,username: str, password: str) -> bool: ...
    def logout(self) -> None: ...

@runtime_checkable
class AdvancedAuth(BasicAuth, Protocol):
    def change_password(selfself,old_password: str, new_password: str) -> bool: ...

    def reset_password(self,email: str) -> bool: ...

    def has_permission(self,permission: str) -> bool: ...


def validate_auth_system(auth_system):
    """验证认证系统是否满足要求"""
    if not isinstance(auth_system, AdvancedAuth):
        missing = []
        if not hasattr(auth_system, "change_password"):
            missing.append('change_password')
        if not hasattr(auth_system, 'reset_password'):
            missing.append('reset_password')
        if not hasattr(auth_system, 'has_permission'):
            missing.append('has_permission')

        raise TypeError(f"认证系统缺少必要方法: {missing}")

    return True

# 测试
class SimpleAuth:
    def login(self, username, password):
        return True

    def logout(self):
        pass


class FullAuth(SimpleAuth):
    def change_password(self, old_password, new_password):
        return True

    def reset_password(self, email):
        return True

    def has_permission(self, permission):
        return True

try:
    validate_auth_system(SimpleAuth())  # 会失败
except TypeError as e:
    print(f"验证失败: {e}")

validate_auth_system(FullAuth())  # 成功
