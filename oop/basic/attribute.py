"""
类属性 vs 实例属性
"""

class Student:
    school = "清华大学" # 类属性（所有实例共享）

    def __init__(self, name, grade):
        self.name = name  # 实例对象
        self.grade = grade

s1 = Student("小明",90)
s2 = Student("小红",95)
print(s1.school)
print(s2.school)

# 修改类属性
Student.school = "北京大学"
print(s1.school)
print(s2.school)

s1.school = "上海交大"
print(s1.school)
print(s2.school)

class MyClass:
    class_attr = "我是类属性" #类属性

    def __init__(self,value):
        self.instance_attr = value # 实例属性

obj1 = MyClass("实例1")
obj2 = MyClass("实例2")

#类属性
print(MyClass.class_attr)
print(obj1.class_attr)
print(obj2.class_attr)

# 实例属性
print(obj1.instance_attr)
print(obj2.instance_attr)



"""
通过实例修改类属性的陷阱
"""
class Test:
    shared_list = [] #类属性

    def __init__(self):
        self.personal_list = []  # 实例属性

t1 = Test()
t2 = Test()

# 正确修改类属性（推荐）
Test.shared_list.append("通过类名修改")
print(t1.shared_list)
print(t2.shared_list)

# 通过实例"修改"类属性（实际创建了实例属性）
t1.shared_list = ["通过实例修改"]
print(t1.shared_list)
print(t2.shared_list)
print(Test.shared_list)


"""
合适的使用场景
"""
class Circle:
    # 类属性：常量、默认值、计数器等
    PI = 3.14159
    total_circles = 0

    def __init__(self, radius):
        # 实例属性：对象特有的数据
        self.radius = radius
        Circle.total_circles += 1

    def area(self):
        return Circle.PI * self.radius ** 2

    @classmethod
    def get_total_circles(cls):
        return cls.total_circles

# 使用
c1 = Circle(5)
c2 = Circle(10)
print(f"面积: {c1.area()}")  # 使用类属性PI计算
print(f"总共创建了 {Circle.get_total_circles()} 个圆")


"""
使用 __slots__ 优化内存
"""

class OptimizedStudent:
    __slots__ = ['name', 'age']  # 限制实例属性

    school = "清华大学"  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 这样就不能动态添加新的实例属性
stu = OptimizedStudent("王五", 21)
stu.grade = 90  # 会报错：AttributeError



