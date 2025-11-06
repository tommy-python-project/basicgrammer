"""
继承
"""

class Animal:

    def __init__(self,name):
        self.name = name

    def speak(self):
        pass #抽象方法

# 子类继承父类
class Cat(Animal):
    def speak(self):
        return f"{self.name} 说：喵喵"

class Dog(Animal):
    def speak(self):
        return f"{self.name} 说: 汪汪"


# 使用
cat = Cat("小花")
dog = Dog("大黄")
print(cat.speak())
print(dog.speak())



"""
多重继承
"""
class A:
    def method_a(self):
        return "来自类 A"

class B:
    def method_b(self):
        return "来自类 B"

class C(A,B):
    def method_c(self):
        return "来自类 C"

obj = C()
print(obj.method_a())
print(obj.method_b())
print(obj.method_c())