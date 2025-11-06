"""
元组类型
"""
from typing import Tuple


# 固定长度元组
def get_coordinates() -> Tuple[float, float]:
    return 40.7128, -74.0060

# 可变长度元组(使用 ...)
def process_data_points(points: Tuple[int,...]) -> float:
    return sum(points)/len(points)

# 混合类型元组
def get_user_info() -> Tuple[int,str,bool]:
    return 1, 'Alice', True

# 使用示例
lat,lon = get_coordinates()
print(lat)
print(lon)
average = process_data_points((1,2,3,4,5))
print(average)

user_id,name, active = get_user_info()
print(user_id)
print(name)
print(active)



