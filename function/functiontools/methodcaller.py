"""
methodcaller - 调用方法
"""

import os
from datetime import datetime
from functools import reduce, partial
from operator import methodcaller



class StringProcessor:

    def __init__(self,text):
        self.text = text

    def uppercase(self):
        return self.text.upper()

    def lowercase(self):
        return self.text.lower()

    def replace(self,old,new):
        return self.text.replace(old,new)

    def split(self,delimiter=''):
        return self.text.split(delimiter)


# 创建对象
processor= StringProcessor("Hello World")

# 1. 调用无参数方法
get_upper = methodcaller('uppercase')
get_lower = methodcaller('lowercase')

print(get_upper(processor))
print(get_lower(processor))

# 2. 调用带参数的方法
replace_space = methodcaller('replace',' ','-')
split_text = methodcaller('split','-')

print(replace_space(processor))
print(split_text(processor))


"""
实际应用场景
1. 字符串处理
"""

strings = [
    "hello world",
    "python programming",
    'functional programming',
    'method caller example'
]

# 创建方法调用器
capitalize_all = methodcaller('capitalize')
title_case = methodcaller('title')
strip_whitespace = methodcaller('strip')
count_spaces = methodcaller('count',' ')

# 应用方法调用器
capitalized = list(map(capitalize_all,strings))
titled = list(map(title_case,strings))
space_counts = list(map(count_spaces,strings))

print("首字母大写：",capitalized)
print("标题格式:", titled)
print("空格数量:", space_counts)


"""
2. 列表操作
"""

class DataProcessor:

    def __init__(self,data):
        self.data = data

    def sort_data(self):
        return sorted(self.data)

    def filter_even(self):
        return [x for x in self.data if x % 2 == 0]

    def multiply_by(self,factor):
        return [x *factor for x in self.data]

    def get_stats(self):
        return {
            'sum': sum(self.data),
            'avg': sum(self.data) / len(self.data),
            'min': min(self.data),
            'max': max(self.data)
        }

# 创建数据处理器
numbers = [3,1,4,1,5,9,2,6]
processor = DataProcessor(numbers)

# 使用方法调用器
sort_method = methodcaller('sort_data')
filter_method = methodcaller('filter_even')
multiply_by_2 = methodcaller('multiply_by',2)
get_stats_method = methodcaller('get_stats')

print("排序:", sort_method(processor))
print("偶数:", filter_method(processor))
print("乘以2:",multiply_by_2(processor))
print("统计:",get_stats_method(processor))

"""
3. 与map和filter组合使用
"""

class EmailValidator:

    def __init__(self,email):
        self.email = email

    def is_valid(self):
        return '@' in self.email and '.' in self.email

    def get_domain(self):
        return self.email.split('@')[-1] if '@' in self.email else None

    def get_username(self):
        return self.email.split('@')[0] if '@' in self.email else None

emails = [
    "user@example.com",
    "invalid-email",
    "admin@test.org",
    "no-at-sign.com",
    "john.doe@company.co"
]

# 创建验证器对象
validators = [EmailValidator(email) for email in emails]

# 过滤有效邮箱
is_valid_method = methodcaller('is_valid')
valid_emails = list(filter(is_valid_method,validators))

print("有效邮箱数量：",len(valid_emails))

# 提取域名
get_domain_method = methodcaller('get_domain')
domains = list(map(get_domain_method,valid_emails))
print("域名列表:", domains)


"""
文件操作
"""
class FileManager:

    def __init__(self,filename):
        self.filename = filename

    def read_content(self):
        try:
            with open(self.filename,'r',encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def write_content(self,content):
        with open(self.filename,'w',encoding='utf-8') as f:
            f.write(content)

    def append_content(self,content):
        with open(self.filename,'a',encoding='utf-8') as f:
            f.write(content)

    def file_exists(self):
        return os.path.exists(self.filename)

# 创建文件管理器
files = [
    FileManager('test1.txt'),
    FileManager('test2.txt'),
    FileManager('test3.txt')
]

# 使用方法调用器检查文件存在
exists_method = methodcaller('file_exists')
existing_files = list(filter(exists_method, files))
print(f"存在的文件数量: {len(existing_files)}")

# 批量写入内容
write_hello = methodcaller('write_content', 'Hello World!')
list(map(write_hello, files))

"""
5. 数据库操作模拟
"""

class DatabaseRecord:

    def __init__(self,id,name,created_at,status):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.status = status

    def is_active(self):
        return self.status == 'active'

    def get_age_days(self):
        delta = datetime.now() - self.created_at
        return delta.days

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'status': self.status
        }

# 创建测试数据
records = [
    DatabaseRecord(1, 'Record A', datetime(2023, 1, 1), 'active'),
    DatabaseRecord(2, 'Record B', datetime(2023, 6, 1), 'inactive'),
    DatabaseRecord(3, 'Record C', datetime(2024, 1, 1), 'active'),
    DatabaseRecord(4, 'Record D', datetime(2022, 12, 1), 'active')
]

# 使用方法调用器处理记录
is_active_method = methodcaller('is_active')
get_age_method = methodcaller('get_age_days')
to_dict_method = methodcaller('to_dict')

# 过滤活跃记录
active_records = list(filter(is_active_method, records))
print(f"活跃记录数量: {len(active_records)}")

# 获取所有记录的年龄
ages = list(map(get_age_method, records))
print("记录年龄(天):", ages)

# 转换为字典
dict_records = list(map(to_dict_method, records))
print("字典格式:", dict_records[:2])  # 只显示前两个


"""
6. web开发模拟
"""
class HTTPRequest:
    def __init__(self,method,path,headers=None,body=None):
        self.method = method
        self.path = path
        self.headers = headers or {}
        self.body = body or {}

    def is_get(self):
        return self.method == 'GET'

    def is_post(self):
        return self.method == 'POST'

    def has_headers(self,header_name):
        return header_name in self.headers

    def get_json_body(self):
        return self.body if isinstance(self.body, dict) else {}

class HTTPResponse:
    def __init__(self,status_code,data):
        self.status_code = status_code
        self.data = data

    def is_success(self):
        return 200 <= self.status_code < 300

    def is_error(self):
        return 400 <= self.status_code

    def to_dict(self):
        return {
            'status_code': self.status_code,
            'data': self.data
        }

# 模拟处理请求
requests = [
    HTTPRequest('GET', '/api/users', {'Authorization': 'Bearer token'}),
    HTTPRequest('POST', '/api/users', {}, {'name': 'John'}),
    HTTPRequest('GET', '/api/products'),
    HTTPRequest('DELETE', '/api/users/1')
]

# 使用方法调用器处理请求
# is_get_method = methodcaller('is_get')
# is_post_method = methodcaller('is_post')
# has_auth_method = methodcaller('has_header', 'Authorization')
#
# get_requests = list(filter(is_get_method, requests))
# post_requests = list(filter(is_post_method, requests))
# auth_requests = list(filter(has_auth_method, requests))
#
# print(f"GET 请求: {len(get_requests)}")
# print(f"POST 请求: {len(post_requests)}")
# print(f"认证请求: {len(auth_requests)}")


"""
7. 与functools组合使用
"""

class NumberList:

    def __init__(self,numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def product(self):
        return reduce(lambda x,y: x*y, self.numbers,1)

    def average(self):
        return self.sum()/ len(self.numbers) if self.numbers else 0

    def apply_operation(self,operation):
        return [operation(x) for x in self.numbers]

# 创建数字列表
number_lists = [
    NumberList([1, 2, 3, 4, 5]),
    NumberList([10, 20, 30]),
    NumberList([2, 4, 6, 8])
]

# 使用方法调用器
sum_method = methodcaller('sum')
avg_method = methodcaller('average')

sums = list(map(sum_method, number_lists))
averages = list(map(avg_method, number_lists))

print("各列表总和:", sums)
print("各列表平均值:", averages)

# 部分应用
square_operation = partial(methodcaller('apply_operation'), lambda x: x ** 2)
squared_lists = list(map(square_operation, number_lists))
print("平方后的列表:", squared_lists)

