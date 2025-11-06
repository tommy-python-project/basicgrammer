from functools import wraps


def cache(func):
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cached_results:
            print(f"从缓存返回 {args}")
            return cached_results[args]
        result = func(*args, **kwargs)
        cached_results[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))