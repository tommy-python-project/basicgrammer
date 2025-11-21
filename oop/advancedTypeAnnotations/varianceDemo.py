"""
协变
"""
from typing import TypeVar, Generic, Iterable, List


class Animal:
    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):
    def speak(self) -> str:
        return "woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

# 协变类型参数
T_co = TypeVar('T_co', covariant=True)

class ReadOnlyBox(Generic[T_co]):
    def __init__(self, value: T_co) -> None:
        self.value = value

    def get(self) -> T_co:
        return self.value

# 协变允许子类型关系
def process_animals(animals: ReadOnlyBox[Animal]) -> None:
    # 我们只能从盒子中读取，不会修改内容
    # 所以即使传入的是 ReadOnlyBox[Dog]，返回 Dog 也是安全的
    # 因为 Dog 是 Animal 的子类型
    for animal in [animals.get()]:
        print(animal.speak())


dog_box: ReadOnlyBox[Dog] = ReadOnlyBox(Dog())
process_animals(dog_box)  # 合法，因为 Dog 是 Animal 的子类型

"""
为什么协变是安全的？
"""
class ReadOnlyBox(Generic[T_co]):
    def __init__(self, value: T_co) -> None:
        self._value = value

    def read(self) -> T_co:
        return self._value

# 协变的安全性分析
dog_box: ReadOnlyBox[Dog] = ReadOnlyBox(Dog())

def use_animal_box(box: ReadOnlyBox[Animal]) -> Animal:
    # 我们只能从盒子中读取，不会修改内容
    # 所以即使传入的是 ReadOnlyBox[Dog]，返回 Dog 也是安全的
    # 因为 Dog 是 Animal 的子类型
    return box.read()

animal: Animal = use_animal_box(dog_box)
print(f"动物说: {animal.speak()}")  # 输出: 动物说: Woof!

"""
内置的协变类型
"""

def count_legs(animals: Iterable[Animal]) -> int:
    return sum(1 for _ in animals)

# Iterable 是协变的，所以这些调用都是合法的
dogs_list: List[Dog] = [Dog(),Dog()]
cats_tuple: tuple[Cat, Cat] = (Cat(), Cat())

count_legs(dogs_list)   # 合法
count_legs(cats_tuple)  # 合法