"""
多重继承与方法解析顺序
"""

class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")
        super().method()

class C(A):
    def method(self):
        print("C.method")
        super().method()

class D(B, C):
    def method(self):
        print("D.method")
        super().method()

# 查看MRO
print(D.__mro__)

d = D()
d.method()


class Writer:
    def write(self, msg):
        print("Writer:", msg)

class Logger:
    def log(self, msg):
        print("Logger:", msg)

class App(Writer, Logger):
    pass

a = App()
a.write("hello")
a.log("bye")
