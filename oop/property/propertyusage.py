"""
@property 计算属性和惰性求值
"""
import time


class ExpensiveComputation:
    def __init__(self,data):
        self._data = data
        self._result = None
        self._computed = False

    @property
    def result(self):
        """惰性求值 - 只在第一次访问时计算"""
        if not self._computed:
            print("正在进行昂贵计算....")
            time.sleep(1) # 模拟耗时操作
            self._result = sum(self._data) * 2  # 模拟复杂计算
            self._computed = True
        return self._result

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,value):
        """当数据改变时，重置计算结果"""
        self._data = value
        self._computed = False

# 使用示例
comp = ExpensiveComputation([1,2,3,4,5])

print("第一次访问结果")
print(comp.result) #会进行计算

print("第二次访问结果")
print(comp.result) # 直接返回缓存结果

# 修改数据会重置缓存
comp.data = [10,20,30]
print("修改数据后访问结果")
print(comp.result) #重新计算