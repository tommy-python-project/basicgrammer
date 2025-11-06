class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        """获取年龄"""
        return self._age
    
    @age.setter
    def age(self, value):
        """设置年龄"""
        if value < 0 or value > 150:
            raise ValueError("年龄不合法")
        self._age = value
    
    @age.deleter
    def age(self):
        """删除年龄属性"""
        del self._age

p = Person("李四", 25)
print(p.age)    # 25（调用 getter）
p.age = 30      # 调用 setter
print(p.age)    # 30
# p.age = -5    # 会抛出 ValueError