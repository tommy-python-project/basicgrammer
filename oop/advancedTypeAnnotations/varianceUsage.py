"""
协变典型应用 --- 数据读取器
"""
from typing import Generic, TypeVar, Iterator

class Animal:
    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):
    def speak(self) -> str:
        return "woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

T_co = TypeVar('T_co', covariant=True)
class DataSource(Generic[T_co]):
    def read_all(self) -> Iterator[T_co]:
        raise NotImplementedError

class AnimalDataSource(DataSource[Animal]):
    def read_all(self) -> Iterator[Animal]:
        yield Dog()
        yield Cat()
        yield Animal()


def process_data_sources(sources: Iterator[DataSource[Animal]]) -> None:
    for source in sources:
        for animal in source.read_all():
            print(animal.speak())

# 创建具体的数据源
dog_source: DataSource[Dog] = AnimalDataSource()  # 协变

# 可以传递给期望 DataSource[Animal] 的函数
process_data_sources(iter([dog_source]))

