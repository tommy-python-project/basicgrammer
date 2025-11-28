"""
yield from - 双向通信
"""

# 1. 定义子生成器
def sub_processor():
    print("--- Sub: 累加器启动 ---")

    total = 0

    # 第一个next() 或 send(None) 启动时，这里的yield 会被执行
    # 然后代码暂停，等待外部 send() 发送数据
    received = yield # 初始接收值，此时 received 为 None

    while received is not None:
        if isinstance(received, int):
            total += received
            print(f"--- Sub: 接收到 {received}, 当前总和: {total}")
        else:
            print(f"--- Sub: 警告，接收到非整数值: {received}")

        # 再次暂停，等待下一个 send() 发送的值
        received = yield total  # 产出当前总和，并再次接收新的输入

    print("--- Sub: 接收到 None，累加结束 ---")
    # 子生成器使用 return 返回结果，该结果将被 yield from 捕获
    return total

# 2. 定义委托生成器（Delegating Generator）
def main_generator():
    print(">>> Main: 主程序启动，准备委托...")

    # 将控制权和通信通道交给 sub_processor
    # sub_result 将捕获 sub_processor 的return 值
    sub_result = yield from sub_processor()

    print(f">>> Main: 委托结束，子生成器返回结果: {sub_result}")

    # 产出最终结果
    yield f"最终总和为: {sub_result}"


# 3 驱动代码（Caller）
"""
驱动代码通过send()方法与生成器进行交互
"""
# 3.1 实例化生成器
g = main_generator()

# 3.2 启动生成器（第一次调用 next() 或 send(None)）
# next() 或 send(None) 会运行到子生成器的第一个yield处
print("\n--- [步骤 1: 启动] ---")
print(next(g))

# 预期输出：>>> Main: 主程序启动... -> --- Sub: 累加器启动 --- -> None (来自 sub_processor 的第一个 yield)

# 3.3 通过 send() 发送数据
print("\n--- [步骤 2: 发送数据 10] ---")
# send(10) 的值 10 直接进入 sub_processor，成为第一个 yield 的值 (received)
# sub_processor 计算 total=10，然后产出 total=10 (暂停)
print(g.send(10))
# 预期输出：--- Sub: 接收到 10, 当前总和: 10 -> 10 (来自 sub_processor 的 yield total)

print("\n--- [步骤 3: 发送数据 20] ---")
# send(20) 的值 20 再次进入 sub_processor
# sub_processor 计算 total=30，然后产出 total=30 (暂停)
print(g.send(20))
# 预期输出：--- Sub: 接收到 20, 当前总和: 30 -> 30 (来自 sub_processor 的 yield total)


# 4. 发送 None 信号，通知子生成器停止
print("\n--- [步骤 4: 发送停止信号 None] ---")
# send(None) 使得 sub_processor 退出 while 循环，执行 return total (30)
# main_generator 捕获 30，继续执行，并产出最终结果
try:
    final_output = next(g)
    print(final_output)
except StopIteration as e:
    # Python 习惯在生成器结束后抛出 StopIteration，其 value 属性通常包含最后的返回值，
    # 但在 yield from 场景下，我们通常关注委托生成器的 yield 值。
    # 这里我们简化为捕获委托生成器最后产出的值。
    pass