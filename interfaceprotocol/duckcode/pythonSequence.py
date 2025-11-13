"""
深入理解python序列
"""

class MySequence:

    def __init__(self,data):
        self._data = list(data)

    def __getitem__(self, index):
        print(f"__getitem__ 被调用，索引: {index}")
        return self._data[index]

    # 注意：我们故意*不*实现 __len__

# --- 测试 ---
seq = MySequence("abcde")

# 1. 索引
print(f"元素 1: {seq[1]}")

# 2. 切片 (Slicing)
# 当 Python 看到 __getitem__ 和一个 slice 对象时，它会自动处理
print(f"切片 1:3: {seq[1:3]}") # 输出: 切片 1:3: ['b', 'c']

# 3. 迭代 (Iteration)
# Python 足够聪明，当它发现 __getitem__ 但没有 __iter__ 时，
# 它会尝试从索引 0 开始调用 __getitem__，直到触发 IndexError。
#print("开始迭代:")
for char in seq:
    print(char)
