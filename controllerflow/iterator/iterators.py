"""
迭代器- 迭代器是实现了迭代器协议的对象，包含__iter__()和__next__()方法
"""

# 自定义迭代器示例
class CountDown:

    def __init__(self,start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current +1

# 使用迭代器
counter = CountDown(5)
for num in counter:
    print(num)

# iter() 函数的工作原理
my_list = [1, 2, 3]
iterator = iter(my_list)  # 调用 my_list.__iter__()
print(next(iterator))     # 1 - 调用 iterator.__next__()
print(next(iterator))     # 2
print(next(iterator))     # 3

