"""
魔术方法入门
"""

class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        """定义 print() 的输出"""
        return f"《{self.title}》，共 {self.pages} 页"

    def __repr__(self):
        """定义对象的表示"""
        return f"Book('{self.title}',{self.pages})"

    def __len__(self):
        """定义 len()的行为"""
        return self.pages

    def __add__(self,other):
        """定义 + 运算符的行为"""
        return self.pages + other.pages

    def __eq__(self,other):
        """定义 == 运算符的行为"""
        return self.pages == other.pages

book1 = Book("Python编程",500)
book2 = Book("数据结构",300)

print(book1)
print(len(book1))
print(book1 + book2)
print(book1 == book2)
