"""
用户自定义的可调用类型
通过实现__call__方法，可以让类的实现像函数一样调用
"""

class Counter:
    """可调用的计数器"""
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

# 创建实例
counter = Counter()
print(counter())
print(counter())
print(counter())

"""
带状态的过滤器
"""
class BetweenFilter:
    """过滤指定范围的值"""
    def __init__(self,low,high):
        self.low = low
        self.high = high

    def __call__(self,value):
        return self.low <= value <= self.high

# 创建过滤器
between_10_20 = BetweenFilter(10,20)
# 创建过滤器
numbers = [5,12,18,25,15,8,22]
filtered = list(filter(between_10_20, numbers))
print(filtered)


"""
记忆化装饰器
"""
class Memoize:
    """缓存函数结果的装饰器"""
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(20))


"""
与闭包比较的优势
"""

# 闭包方式
def make_averager():
    series = []
    def averager(value):
        series.append(value)
        return sum(series) / len(series)
    return averager

# 可调用类方式
class Averager:

    def __init__(self):
        self.series = []

    def __call__(self, value):
        self.series.append(value)
        return sum(self.series) / len(self.series)

# 使用
avg1 = make_averager()
avg2 = Averager()

print(avg1(10))
print(avg2(10))

# 类的优势：可以访问和修改内部状态
print(avg2.series)



