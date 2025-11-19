"""
钻石问题（diamond）与协作式 super()（逐步演示）

目标：让 A 的方法只执行一次且 B、C、D 的方法按 MRO 顺序调用。示例：
"""

class A:

    def __init__(self, *args, **kwargs):
        print("A.__init__")
        super().__init__(*args, **kwargs)

    def do(self):
        print("A.do")

class B(A):
    def __init__(self, *args, **kwargs):
        print("B.__init__ start")
        super().__init__(*args, **kwargs)
        print("B.__init__ end")

    def do(self):
        print("B.do start")
        super().do()
        print("B.do end")

class C(A):
    def __init__(self, *args, **kwargs):
        print("C.__init__ start")
        super().__init__(*args, **kwargs)
        print("C.__init__ end")

    def do(self):
        print("C.do start")
        super().do()
        print("C.do end")

class D(B, C):
    def __init__(self, *args, **kwargs):
        print("D.__init__ start")
        super().__init__(*args, **kwargs)
        print("D.__init__ end")

    def do(self):
        print("D.do start")
        super().do()
        print("D.do end")

print("MRO:", [c.__name__ for c in D.mro()])
D().do()

