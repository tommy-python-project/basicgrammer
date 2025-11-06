"""
闭包 vs 类
有时闭包可以替代简单的类
"""

# 使用闭包
def make_averager():
    series = []

    def averager(value):
        series.append(value)
        return sum(series) / len(series)

    return averager


# 使用类
class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, value):
        self.series.append(value)
        return sum(self.series) / len(self.series)

# 两者用法相似
avg1 = make_averager()
avg2 = Averager()

print(avg1(10))  # 10.0
print(avg2(10))  # 10.0