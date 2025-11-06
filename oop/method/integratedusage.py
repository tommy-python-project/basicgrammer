"""
类方法 vs 静态方法 vs 实例方法 综合使用
日期处理
"""
import datetime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def display(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    # 类方法：替代构造函数
    @classmethod
    def from_string(cls,date_string):
        """从字符串 'YYYY-MM-DD' 创建Date实例 """
        year,month,day = map(int,date_string.split('-'))
        return cls(year,month,day)

    @classmethod
    def from_timestamp(cls,timestamp):
        """从时间戳创建Date实例"""
        dt = datetime.datetime.fromtimestamp(timestamp)
        return cls(dt.year,dt.month,dt.day)

    # 静态方法：工具函数
    @staticmethod
    def is_leap_year(year):
        """判断是否为闰年"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def is_valid_date(year,month,day):
        """验证日期有效"""
        if month < 1 or month > 12:
            return False
        days_in_month  = [31,29 if Date.is_leap_year(year) else 28,31,30,31,30,31,31,30,31,30,31,31,30,31,30,31]

        return 1 <= day <= days_in_month[month-1]

# 使用示例
# 实例方法
d1 = Date(2023,10,15)
print(d1.display())

# 类方法
d2 = Date.from_string("2021-10-15")
d3 = Date.from_timestamp(1695000000)

# 静态方法
print(Date.is_leap_year(2024))  # True
print(Date.is_valid_date(2023, 2, 29))  # False