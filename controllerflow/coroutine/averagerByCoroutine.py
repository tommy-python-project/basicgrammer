"""
用协程计算累计平均值
"""

def averager():
    total = 0.0
    count = 0
    average = None

    print("平均值计算器启动...")

    while True:
        try:
            # data 接收 send() 发送的值
            data = yield average

            total += data
            count += 1
            average = total / count
            print(f"累计数据: {data} | 累计总和: {total} | 累计平均值: {average:.2f}")


        except GeneratorExit:
            print("\n平均值计算器关闭。最终平均值:", average)
            break
        except TypeError:
            # 处理 send(None) 等非数字输入
            pass

# 创建并预激协程
avg_coroutine = averager()
next(avg_coroutine) # 预激：执行到第一个yield处暂停

print("-" * 20)

# 发送数据
avg_coroutine.send(10) # 接收 10，计算平均值 10.00
avg_coroutine.send(20) # 接收 20，计算平均值 15.00
avg_coroutine.send(30) # 接收 30，计算平均值 20.00

print("-" * 20)

# 关闭协程
avg_coroutine.close()