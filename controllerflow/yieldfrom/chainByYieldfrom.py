"""
yield from 表达式重新实现chain
"""

def my_chain(*iterables):
    for iterable in iterables:
        yield from iterable

result = my_chain([1,2,3], (4,5,6),'abc')
print(list(result))