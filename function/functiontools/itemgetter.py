"""
itemgetter - 获取元素
"""

from operator import itemgetter

# 单个索引
data = [('Alice', 30, 'NYC'), ('Bob', 25, 'LA'), ('Charlie', 35, 'SF')]
get_name = itemgetter(0)
get_age = itemgetter(1)

print([get_name(item) for item in data])  # ['Alice', 'Bob', 'Charlie']

# 多个索引
get_name_age = itemgetter(0, 1)
print([get_name_age(item) for item in data])
# [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

# 字典
person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
get_name = itemgetter('name')
print(get_name(person))  # Alice

"""
itemgetter实际应用场景
1、列表排序
"""

# 对元组列表按特定字段排序
students = [
    ('Alice',85,'Math'),
    ('Bob',92,'Science'),
    ('Charlie',78,'Math'),
    ('David',95,'Science'),
]

# 按分数排序（第二个元素）
sorted_by_score = sorted (students, key = itemgetter(1))
print("按分数排序：",sorted_by_score)

# 按科目然后按分数排序
sorted_by_subject_score = sorted(students,key=itemgetter(2,1))
print("按科目和分数排序:", sorted_by_subject_score)


"""
2. 字典操作
"""
data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'London'},
    {'name': 'Charlie', 'age': 22, 'city': 'Paris'},
    {'name': 'Diana', 'age': 28, 'city': 'San Jose'},
]

# 按年龄排序
sorted_by_age = sorted(data,key = itemgetter('age'))
print("按年龄排序：",sorted_by_age)

# 获取多个字段
get_name_city = itemgetter('name','city')
names_cities = [get_name_city(person) for person in data]
print("姓名和城市：",names_cities)


"""
3. 与map和filter结合使用
"""

# 提取特定字段
transactions = [
    ('2023-01-01','Alice',100),
    ('2023-01-02','Bob',200),
    ('2023-01-03','Charlie',150),
]

# 提取所有金额
amounts = list(map(itemgetter(2),transactions))
print("所有金额：",amounts)

# 提取所有姓名
names = list(map(itemgetter(1),transactions))
print(f"所有姓名：{names}")

"""
在数据处理中的应用
"""

# 复杂数据结构处理
company_data = [
    {'department':'Sales','employees':[
        {'name':'Alice','salary':50000},
        {'name':'Bob','salary':20000},
    ]},
    {'department': 'IT', 'employees': [
        {'name': 'Charlie', 'salary': 70000},
        {'name': 'Diana', 'salary': 80000}
    ]}
]

# 获取所有部门名称
departments = list(map(itemgetter('department'),company_data))
print(f"部门：{departments}")


# 获取最高薪水
get_salary = itemgetter('salary')
all_salaries = []
for dept in company_data:
    dept_salaries = list(map(get_salary, dept['employees']))
    all_salaries.extend(dept_salaries)

max_salary = max(all_salaries)
print("最高薪水:", max_salary)

"""
6. 嵌套数据结构
"""

# 处理嵌套数据结构
nested_data = [
    {'user':{'id':1,'profile':{'name':'Alice','age':25}}},
    {'user': {'id': 2, 'profile': {'name': 'Bob', 'age': 30}}},
    {'user': {'id': 3, 'profile': {'name': 'Charlie', 'age': 22}}}
]

# 创建自定义获取器
def nested_getter(*keys):
    def getter(obj):
        result = obj
        for key in keys:
            result = result[key]
        return result
    return getter

# 获取所有用户名
get_names = nested_getter('user','profile', 'name')
names = list(map(get_names,nested_data))
print(f"用户名: {names}")

