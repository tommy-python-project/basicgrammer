"""
协程的装饰器和状态检查
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
def running_averager():
    """使用装饰器的协程"""
    total= 0.0
    count = 0
    average = None

    while True:
        value = yield average
        total += value
        count += 1
        average = total / count

def demo_running_averager():
    # 不需要手动调用next()了
    avg = running_averager()

    print(f"协程状态: {avg.gi_frame.f_lasti}")  # 查看协程状态

    print(avg.send(5))  # 5.0
    print(avg.send(15))  # 10.0
    print(avg.send(25))  # 15.0

    print(f"协程代码对象: {avg.gi_code.co_name}")

demo_running_averager()


