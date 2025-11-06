"""
完整的自定义魔术方法
"""

class Matrix:

    """一个支持各种操作的矩阵类"""

    def __init__(self,data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        """友好的字符串表示"""
        return '\n'.join([' '.join(map(str,row)) for row in self.data])

    def __repr__(self):
        """可重建的表示"""
        return f"Matrix({self.data})"

    def __add__(self,other):
        """矩阵加法"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self,other):
        """标量乘法或矩阵乘法"""
        if isinstance(other,(int,float)):
            # 标量乘法
            result = []
            for row in self.data:
                result.append([elem * other for elem in row])
            return Matrix(result)
        elif isinstance(other,Matrix):
            # 矩阵乘法
            if self.cols != other.rows:
                raise ValueError("Invalid dimensions for matrix multiplication")

            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    sum_val = 0
                    for k in range(self.cols):
                        sum_val += self.data[i][k] * other.data[k][j]
                    row.append(sum_val)
                result.append(row)
            return Matrix(result)

    def __getitem__(self,key):
        """支持索引访问"""
        if isinstance(key,tuple):
            row, col = key
            return self.data[row][col]
        else:
            return self.data[key]

    def __setitem__(self,key,value):
        """支持索引赋值"""
        if isinstance(key,tuple):
            row, col = key
            self.data[row][col] = value
        else:
            self.data[key] = value

    def __eq__(self,other):
        """判断相等"""
        return self.data == other.data

    def __bool__(self):
        """布尔值判断"""
        return self.rows > 0 and self.cols > 0

# 使用示例
m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[5,6],[7,8]])

print("Matrix 1:")
print(m1)
print("\nMatrix 2:")
print(m2)
print("\nAddition:")
print(m1 + m2)
print("\nScalar multiplication:")
print(m1 * 2)
print("\nElement access:")
print(m1[0, 1])  # 2