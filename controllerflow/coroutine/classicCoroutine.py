"""
经典协程- 双向通信与预激
"""

def consumer():

    print("消费者启动，等待接收第一个数据...")
    # 第一次 next() 或 send(None) 会执行到这里

    total = 0
    count = 0

    while True:
        # data = yield 这里的 data 接收 send() 发送的值
        # yield 后面的 None 是返回给 send（）调用者的值（通常是 None）
        try:
            data = yield None
            if data is None:
                # 收到 None 视为结束或特殊信号
                break

            total += data
            count += 1
            print(f"消费者：接收到 {data}。当前总和: {total}")
        except GeneratorExit :
            # 协程被 close() 时会捕获此异常
            print("\n消费者关闭。")
            break

    # 计算并返回平均值（在经典协程中，返回值通常通过 StopIteration 一场传递）
    return total / count if count else 0

def producer(c):

    # 1. 预激协程：执行到第一个yield 处暂停
    c.send(None)
    print("生产者启动...")

    # 2. 发送数据给协程
    data_list = [10,20,30,40,50]
    for n in data_list:
        print(f"生产者：发送 {n}")
        # send(n) 发送数据，并恢复协程执行到下一个 yield
        # c.send(n) 的返回值是 yield 后面表达式的值（这里是 None）
        c.send(n)


    # 3. 关闭协程，获取结果
    try:
        c.close() # 或者在 for 循环结束后让协程自然结束
    except StopIteration as e:
        # Python 的生成器协议规定：生成器函数的返回值通过 StopIteration 异常的 value 属性传递
        average = e.value
        print(f"\n计算完成。平均值是: {average}")

# 创建协程对象
c = consumer()
# 运行生产者逻辑
producer(c)

