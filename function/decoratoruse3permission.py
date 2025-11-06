from functools import wraps


def require_permission(permission):
    def decorator(func):

        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not hasattr(user, 'permissions'):
                raise PermissionError("用户没有权限属性")
            if permission not in user.permissions:
                raise PermissionError(f"需要 {permission} 权限")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

class User:
    def __init__(self, name,permissions):
        self.name = name
        self.permissions = permissions

@require_permission('admin')
def delete_user(user,target):
    print(f"{user.name} 删除了 {target}")

admin = User("Alice",['admin','user'])
normal_user = User("Bob",['user'])

delete_user(admin,"Charlie")
delete_user(normal_user, "Charlie")
