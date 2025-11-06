"""
类方法的应用
"""
class Person:
    species = "人类"
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    # 类方法：创建特定类型的对象
    @classmethod
    def create_baby(cls,name):
        """创建一个婴儿 （年龄为0）"""
        return cls(name, 0)

    # 类方法：访问和修改类属性
    @classmethod
    def get_population(cls):
        return cls.population

    # 类方法：替代构造函数
    @classmethod
    def from_dict(cls,data_dict):
        """从字典创建Person实例"""
        return cls(data_dict['name'], data_dict['age'])


# 使用类方法
p1 = Person("张三",25)
baby = Person.create_baby("李小宝")
print(baby.age) # 0

data = {'name':'王五','age':18}
p2 = Person.from_dict(data)      # 从字典创建
print(p2.name)

print(f"总人口：{Person.get_population()}")
