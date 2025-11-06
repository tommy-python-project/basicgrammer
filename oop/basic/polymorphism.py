"""
多态
"""

class Shap:
    def area(self):
        pass

class Rectangle(Shap):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class  Circle(Shap):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

# 多态应用
def print_area(shape):
    print(f"面积是：{shape.area()}")

    
rect = Rectangle(5, 10)
circle = Circle(7)

print_area(rect)    # 面积是：50
print_area(circle)  # 面积是：153.86
