"""
增强版等差数列
"""

class ArithmeticProgression:
    """功能完整的等差数列生成器"""

    def __init__(self,start,stop=None,step=1):
        if step == 0:
            raise ValueError("步长不能为0")

        if stop is None:
            start, stop = 0, start

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        current = self.start
        while (self.step > 0 and current < self.stop) or \
                (self.step < 0 and current > self.stop):
            yield current
            current += self.step

    def __len__(self):
        """计算序列长度"""
        if (self.step > 0 and self.start >= self.stop) or \
                (self.step < 0 and self.start <= self.stop):
            return 0

        return int((self.stop - self.start) / self.step)

    def __getitem__(self, index):
        """支持索引访问"""
        if index < 0:
            index = len(self) + index

        if index < 0 or index >= len(self):
            raise IndexError("索引超出范围")

        return self.start + index * self.step


def advanced_arithmetic_demo():
    print("=== 增强版等差数列 ===")

    ap = ArithmeticProgression(0, 10, 2)
    print(f"序列: {list(ap)}")
    print(f"长度: {len(ap)}")
    print(f"第三个元素: {ap[2]}")
    print(f"最后一个元素: {ap[-1]}")

    # 支持负步长
    ap2 = ArithmeticProgression(10, 0, -2)
    print(f"递减序列: {list(ap2)}")

advanced_arithmetic_demo()


