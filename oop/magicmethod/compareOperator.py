"""
比较运算符
"""
class Box:

    def __init__(self, size):
        self.size = size

    def __eq__(self, other):
        """等于： =="""
        return self.size == other.size

    def __ne__(self, other):
        """不等于：!="""
        return self.size != other.size

    def __lt__(self, other):
        """小于：<="""
        return self.size < other.size

    def __le__(self, other):
        """小于等于： <="""
        return self.size <= other.size

    def __gt__(self, other):
        """大于: > """
        return self.size > other.size

    def __ge__(self, other):
        """大于等于：>="""
        return self.size >= other.size

# 使用示例
box1 = Box(10)
box2 = Box(20)
print(box1 < box2)
print(box1 == box2)