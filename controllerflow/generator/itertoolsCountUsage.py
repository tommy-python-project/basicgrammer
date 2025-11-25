"""
使用itertools模块生成等差数列
"""
import itertools
from datetime import datetime, timedelta


# 案例1 ： 数据采样
def data_sampling():
    """使用等差数列进行数据采样"""

    # 模拟大数据集
    big_dataset = range(1000000)

    # 每100个数据采样一个
    sample_indices = itertools.islice(
        itertools.count(0,100),# 0, 100, 200, ...
        100 # 只取100个样本
    )

    samples = [big_dataset[i] for i in sample_indices]
    print(f"采样数据: {samples[:10]}...")  # 显示前10个样本

data_sampling()

# 时间序列生成
def time_sequence_generator():
    """生成时间序列"""

    start_time = datetime(2024, 1, 1, 0, 0, 0)
    time_delta = timedelta(hours=1)

    # 生成24小时的时间序列
    time_sequence = (
        start_time + i * time_delta
        for i in range(24)
    )

    print("24小时时间序列:")
    for time_point in time_sequence:
        print(time_point.strftime("%Y-%m-%d %H:%M:%S"))

time_sequence_generator()


# 数值积分采样
def numerical_integration():
    """私用等差数列进行数值积分采样"""

    def f(x):
        return x ** 2 # 函数 f(x) = x²

    # 在区间 [0, 1] 上采样
    a, b = 0, 1
    n_samples = 10

    # 生成采样点
    samples = (a + i * (b - a) / n_samples for i in range(n_samples + 1))

    # 计算黎曼和
    integral = sum(f(x) * (b - a) / n_samples for x in samples)
    exact_value = 1 / 3  # ∫x²dx from 0 to 1 = 1/3

    print(f"数值积分结果: {integral:.6f}")
    print(f"精确值: {exact_value:.6f}")
    print(f"误差: {abs(integral - exact_value):.6f}")

numerical_integration()