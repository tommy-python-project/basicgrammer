"""
支持位置的模式匹配
"""

class Position:
    # 指定匹配时按顺序提取这两个属性
    __match_args__ = ('lat','lon')

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


def describe_position(pos):
    match pos:
        case Position(lat,lon) if lat > 0 :
            print(f"Northern Hemisphere at latitude {lat}")
        case Position(lat=0, lon=0):
            print("The Origin!")
        case _:
            print("Other position.")

p1 = Position(40.71,-74.01)

# 匹配时，Position(lat, lon) 会按 __match_args__ 的顺序提取属性值
describe_position(p1)