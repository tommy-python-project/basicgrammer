"""
yield from (High-Level Delegation)
"""

def sub_generator(x):
    for i in range(x):
        yield i

def delegating_generator():
    # 委托生成器将控制权交给 sub_generator
    yield from sub_generator(3)
    yield "Done"

# 结果：0, 1, 2, Done

"""
捕获子生成器的返回值
"""

def sub_processor():
    # 子生成器在结束时返回一个值
    yield "Processing..."
    return 42

def main_processor():
    # 委托生成器捕获子生成器的返回值
    result = yield from sub_processor()
    print(f"Subprocessor returned: {result}")
    yield result * 2

# 运行过程：
g = main_processor()
print(next(g))  # 输出: Processing... (来自 sub_processor 的 yield)
# 当再次调用 next(g) 时，sub_processor 结束并 return 42
# 42 被赋值给 result
# 委托生成器继续执行 print 和 yield 84
print(next(g)) # 输出: Subprocessor returned: 42 (来自 print)
# 输出: 84 (来自 main_processor 的 yield)