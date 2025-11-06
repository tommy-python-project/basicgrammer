"""
attrgetter- 获取属性
"""
from dataclasses import dataclass
from functools import reduce
from operator import attrgetter
from typing import List


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name},{self.age})"

people = [
    Person('Alice', 30),
    Person('Bob', 25),
    Person('Charlie', 35),
]

# 按年龄排序
sorted_people = sorted(people,key=attrgetter('age'))
print(sorted_people)

# 获取多个属性
get_info = attrgetter('name','age')
print([get_info(p) for p in people])

# 嵌套属性
class Address:
    def __init__(self,city,country):
        self.city = city
        self.country = country

class PersonWithAddress:
    def __init__(self,name,address):
        self.name = name
        self.address = address

people = [
    PersonWithAddress('Alice',Address('NYC','UAS')),
    PersonWithAddress('Bob', Address('London', 'UK'))
]

# 获取嵌套属性
get_city = attrgetter('address.city')
print([get_city(p) for p in people])


"""
attrgetter 实际应用场景
"""

"""1. 对象排序"""
class Product:

    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product({self.name},{self.price},{self.category})"

products = [
    Product('Laptop',999,'Electronics'),
    Product('Book',25,'Education'),
    Product('Phone',699,'Electronics'),
    Product('Pen',2,'Office'),
]

# 按价格排序
sorted_by_price = sorted(products,key=attrgetter('price'))
print(f"按价格排序：{sorted_by_price}")

# 按类别然后按照价格排序
sorted_by_category_price = sorted(products,key=attrgetter('category','price'))
print(f"按类别和价格排序：{sorted_by_category_price}")

# 按名称长度（结合 lambda）
sorted_by_name_length = sorted(products,key=lambda p : len(attrgetter('name')(p)))
print("按名称长度排序：",sorted_by_name_length)

"""
2. 与map 和filter结合使用
"""

class Employee:

    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

employees = [
    Employee('Alice',5000,'Engineering'),
    Employee('Bob',7500,'Sales'),
    Employee('Charlie',6000,'Engineering'),
    Employee('David',8000,'Marketing'),
]

# 提取所有姓名
names = list(map(attrgetter('name'),employees))
print(f"所有员工姓名：: {names}")

# 提取高薪员工的姓名
high_salary_names = [ emp.name for emp in employees if attrgetter('salary')(emp) > 6000]
print("高薪员工:", high_salary_names)

# 使用 map 获取 所有薪水
salaries = list(map(attrgetter('salary'),employees))
print("所有薪水：",salaries)


"""
嵌套属性访问
"""

class Address:

    def __init__(self,street,city,country):
        self.street = street
        self.city = city
        self.country = country

class Company:

    def __init__(self,name,address):
        self.name = name
        self.address = address

class Employee:
    def __init__(self,name,company):
        self.name = name
        self.company = company

# 创建嵌套对象
address = Address('123 Main St', 'San Francisco', 'USA')
company = Company('Tech Corp', address)
employee = Employee('John Doe', company)

# 访问嵌套属性
get_city = attrgetter('company.address.city')
get_company_country = attrgetter('company.address.country')


print("员工所在城市:", get_city(employee))      # 输出: San Francisco
print("公司所在国家:", get_company_country(employee))  # 输出: USA


"""
4. 在数据处理管道中的应用
"""

class Sale:
    def __init__(self,product,quantity,price):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.revenue = quantity * price


sales = [
    Sale('Laptop', 2, 999),
    Sale('Mouse', 10, 25),
    Sale('Keyboard', 5, 75),
    Sale('Monitor', 3, 299)
]

# 计算总营收
total_revenue = reduce(
    lambda a,b: a+b,
    map(attrgetter('revenue'),sales)
)
print(f"总营收: ${total_revenue}")

# 找到营收最高的销售
highest_sale = max(sales,key=attrgetter('revenue'))
print(f"最高营收销售: {highest_sale.product}, ${highest_sale.revenue}")

# 按产品名称排序
sorted_sales = sorted(sales,key=attrgetter('product'))
print("按产品名称排序:", [sale.product for sale in sorted_sales])


"""
6. 高级用法：动态访问属性
"""

class Config:
    def __init__(self):
        self.database_host = 'localhost'
        self.database_port = 5432
        self.api_timeout = 30
        self.cache_size = 1000

config = Config()

# 动态获取配置属性
config_keys = ['database_host', 'database_port', 'api_timeout']

for key in config_keys:
    getter = attrgetter(key)
    valuer = getter(config)
    print(f"{key}: {valuer}")

# 批量获取配置
get_config_values = attrgetter(*config_keys)
values = get_config_values(config)
print("配置值：",dict(zip(config_keys,values)))


"""
7. 在实际项目中的应用
"""

@dataclass
class OrderItem:
    product: str
    quantity: int
    unit_price: float

    @property
    def total_price(self):
        return self.quantity * self.unit_price





@dataclass
class Order:
    order_id: int
    customer: str
    items:List[OrderItem]

    @property
    def order_total(self):
        return sum(item.total_price for item in self.items)

# 创建订单数据
orders = [
    Order(1,'Alice',[
        OrderItem('Book',2,15.99),
        OrderItem('Pen',5,1.99),
    ]),
    Order(2,'Bob',[
        OrderItem('Laptop',1,999.99),
        OrderItem('Mouse',1,25.99)
    ])
]

# 按订单总额排序
sorted_orders = sorted(orders,key= attrgetter('order_total'),reverse=True)
print("按订单总额排序：")
for order in sorted_orders:
    print(f" 订单 {order.order_id}: ${order.order_total:.2f}")
    
# 获取所有客户名称
customers = list(map(attrgetter('customer'),orders))
print("所有客户:",customers)