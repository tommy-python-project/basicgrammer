"""
动态协议 - 鸭子类型
"""

# 任何实现了__len__ 和 __getitem__的对象都是序列
class MySequence:

    # def __len__(self):
    #     return 10

    def __getitem__(self, index):
        return index * 2

# 这个类自动支持序列操作
seq = MySequence()
#print(len(seq))  # 10
print(seq[5])    # 10