"""
使用yield from委托生成器
"""

def sub_coroutine():
    """子协程"""
    result = 0
    while True:
        value = yield
        if value is None:
            break
        result += value
    return result

def delegator():
    """委托协程， 使用yield from管理子协程"""
    while True:
        # yield from 会自动处理子协程的启动、值和停止
        result = yield from sub_coroutine()
        print(f"子协程结果: {result}")

def demo_delegator():
    del_coroutine = delegator()
    next(del_coroutine)

    # 发送数据给委托协程，它会自动转发给子协程
    del_coroutine.send(10)
    del_coroutine.send(20)
    del_coroutine.send(None)  # 结束当前子协程，输出: 子协程结果: 30

    del_coroutine.send(5)
    del_coroutine.send(15)
    del_coroutine.send(None)  # 输出: 子协程结果: 20

    del_coroutine.close()

demo_delegator()
