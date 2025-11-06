"""
闭包基本示例
"""

def outer(x):
    def inner(y):
        return x + y  # x 是自由变量
    return inner

add_5 = outer(5)
add_10 = outer(10)



print(add_5(3))   # 8
print(add_10(3))  # 13

# 查看闭包信息
print(add_5.__closure__)  # (<cell at 0x1059c65f0: int object at 0x105692080>,)
print(add_5.__closure__[0].cell_contents)  # 5