"""
泛化容器
"""
from typing import List, Dict, Set


# 列表类型提示
def process_numbers(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]

# 字典类型提示
def create_user_map(users: List[str]) -> Dict[str, int]:
    return {user: len(user) for user in users}

# 集合类型提示
def find_common_elements(a: Set[int], b: Set[int]) -> Set[int]:
    return a.intersection(b)

# 使用示例
numbers = process_numbers([1,2,3,4])
print(numbers)
user_map = create_user_map(['Alice','Bob'])
print(user_map)
common = find_common_elements({1,2,3},{2,3,4})
print(common)