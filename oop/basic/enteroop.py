"""
面向对象入门
类和对象
"""

#定义一个类
class Dog:
    # 构造函数
    def __init__(self, name,age):
        self.name = name # 实例属性
        self.age = age

    # 实例方法
    def bark(self):
        return f'{self.name} 汪汪叫.'

    def get_info(self):
        return f'{self.name} is {self.age} years old.'


# 创建对象（实例化）
my_dog = Dog("旺财",3)
print(my_dog.bark())
print(my_dog.get_info())