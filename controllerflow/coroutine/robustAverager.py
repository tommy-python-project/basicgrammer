"""
协程异常处理
"""
from functools import wraps


def coroutine(func):
    """协程装饰器，自动预激协程"""

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen) # 预激协程
        return gen
    return primer


@coroutine
def robust_averager():
    """带有异常处理的协程"""
    total = 0.0
    count = 0
    average = None

    while True:
        try:
            value = yield average
            total += value
            count += 1
            average = total / count
        except ZeroDivisionError:
            average = 0
            yield "错误：除零错误，平均值重置为0"
        except TypeError:
            yield "错误：请输入数字"

def demo_robust_averager():
    avg = robust_averager()

    print(avg.send(10))  # 10.0
    print(avg.send("abc"))  # 错误：请输入数字
    print(avg.send(20))  # 15.0

    # 模拟除零错误
    problematic_avg = robust_averager()
    print(problematic_avg.send(0))  # 0.0

demo_robust_averager()
