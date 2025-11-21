"""
逆变
"""
from typing import TypeVar, Generic, Callable, List


class Animal:
    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):
    def speak(self) -> str:
        return "woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

T_contra = TypeVar('T_contra', contravariant=True)

class Writer(Generic[T_contra]):
    def __init__(self,write_func: Callable[[T_contra], None]):
        self._write_func = write_func

    def write(self,value: T_contra) -> None:
        self._write_func(value)


# 逆变例子
def animal_printer(animal: Animal) -> None:
    print(f"Animal: {animal.speak()}")

def dog_printer(dog: Dog) -> None:
    print(f"Dog: {dog.speak()}")


# 逆变允许反向子类型关系
animal_writer: Writer[Animal] = Writer(animal_printer)
dog_writer: Writer[Dog] = Writer(dog_printer)


# 这是合法的，因为 Writer[Animal] 可以接受 Writer[Dog]
# 在需要处理 Animal 的地方，我们可以使用处理 Dog的 Writer
def use_writer(writer: Writer[Dog]) -> None:
    writer.write(Dog())


use_writer(animal_writer) # 合法，因为 Writer[Animal] 是 Writer[Dog] 的子类型


"""
逆变定义：如果 B 是 A 的子类型，那么 Container[A] 是 Container[B] 的子类型
"""

T_contra = TypeVar('T_contra', contravariant=True)

class Consumer(Generic[T_contra]):
    """消费者 - 逆变容器"""
    def __init__(self,callback: Callable[[T_contra], None]):
        self._callback = callback

    def consume(self,item: T_contra) -> None:
        self._callback(item)

# 逆变示例
def animal_consumer(animal: Animal) -> None:
    print(f"处理动物: {animal.speak()}")

def dog_consumer(dog: Dog) -> None:
    print(f"专门处理狗: {dog.speak()}")

# 创建消费者
animal_handler: Consumer[Animal] = Consumer(animal_consumer)
dog_handler: Consumer[Dog] = Consumer(dog_consumer)

def feed_dog(consumer: Consumer[Dog]) -> None:
    """这个函数需要一个能处理 Dog 的消费者"""
    consumer.consume(Dog())

# 逆变允许：Consumer[Animal] 可以当作 Consumer[Dog] 使用
feed_dog(animal_handler)  # 这是合法的！
# feed_dog(dog_handler)    # 当然这也是合法的

print("逆变示例成功执行")

"""
为什么逆变是安全的？
"""

class Writer(Generic[T_contra]):
    def __init__(self) -> None:
        self._data: List[T_contra] = []

    def write(self,item: T_contra) -> None:
        self._data.append(item)

# 逆变的安全性分析
def process_dog_writer(writer: Writer[Dog]) -> None:
    # 这个函数期望一个能写入 Dog 的写入器
    writer.write(Dog())

# 创建一个能写入任何 Animal 的写入器
animal_writer : Writer[Animal] = Writer()

# 为什么这是安全的？
# Writer[Animal] 可以处理 Animal 及其所有子类型
# 当我们调用 write(Dog()) 时，Dog 是 Animal 的子类型
# 所以 Writer[Animal] 完全能够处理 Dog
process_dog_writer(animal_writer)

# 但反过来就不安全：
# Writer[Dog] 只能处理 Dog，不能处理其他 Animal
# 所以不能把 Writer[Dog] 当作 Writer[Animal] 使用

"""
内置的逆变类型
"""

def call_with_dog(func: Callable[[Dog], str]) -> str:
    """接受一个处理 Dog 的函数"""
    return func(Dog())

# 这些函数都可以作为参数传入
def handle_animal(animal: Animal) -> str:
    return f"处理动物: {animal.speak()}"

def handle_dog(dog: Dog) -> str:
    return f"处理狗: {dog.speak()}"

# Callable 参数是逆变的
result1 = call_with_dog(handle_animal)  # 合法 - 逆变
result2 = call_with_dog(handle_dog)     # 合法
print(result1)
print(result2)