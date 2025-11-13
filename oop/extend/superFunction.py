"""
super() 函数
"""

"""
super() 与 MRO
"""

class A:
    def __init__(self):
        print("Initializing A")
        super().__init__()
        print("Finishing A")

class B(A):
    def __init__(self):
        print("Initializing B")
        super().__init__()
        print("Finishing B")

class C(A):
    def __init__(self):
        print("Initializing C")
        super().__init__()
        print("Finishing C")

class D(B, C):
    def __init__(self):
        print("Initializing D")
        super().__init__()
        print("Finishing D")


print("Creating D object:")
d = D()

print("\nMRO for D:")
print(D.mro())