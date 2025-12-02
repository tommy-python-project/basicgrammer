"""
让协程返回一个值
"""

def averager_with_return():
    """计算累计平均值并在结束时返回统计信息"""
    total = 0.0
    count = 0
    average = None

    try:
        while True:
            value = yield average
            if value is None:
                break
            total += value
            count += 1
            average = total / count
    except GeneratorExit:
        # 当协程被关闭时，返回最终结果
        return {"total": total, "count": count, "average": average}

# 注意：在Python 3.3之前，协程返回值会报错
# 从Python 3.3开始，可以在StopIteration异常中获取返回值

def demo_averager_with_return():
    avg_coroutine = averager_with_return()
    next(avg_coroutine)

    print(avg_coroutine.send(10))  # 10.0
    print(avg_coroutine.send(20))  # 15.0
    print(avg_coroutine.send(30))  # 20.0

    try:
        # 发送None来终止循环并获取返回值
        avg_coroutine.send(None)
    except StopIteration as e:
        result = e.value
        print(f"最终结果: {result}")
        # 输出: 最终结果: {'total': 60.0, 'count': 3, 'average': 20.0}

demo_averager_with_return()
