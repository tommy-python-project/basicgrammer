def modify_number(x):
    print(f"函数内修改前: x={x}, id={id(x)}")
    x = x + 10  # 创建新对象
    print(f"函数内修改后: x={x}, id={id(x)}")
    return x

def modify_list(lst):
    print(f"函数内修改前: lst={lst}, id={id(lst)}")
    lst.append(4)  # 修改原对象
    print(f"函数内修改后: lst={lst}, id={id(lst)}")

def append_to(element, target=[]):
    target.append(element)
    return target



num = 5
print(f"调用前: num={num}, id={id(num)}")
result = modify_number(num)
print(f"调用后: num={num}, id={id(num)}")
print(f"返回值: result={result}, id={id(result)}")

print("============================")
my_list = [1, 2, 3]
print(f"调用前: my_list={my_list}, id={id(my_list)}")
modify_list(my_list)
print(f"调用后: my_list={my_list}, id={id(my_list)}")



print("============================")
print(append_to(1))  # [1]
print(append_to(2))  # [1, 2]  ← 注意！不是 [2]
print(append_to(3))  # [1, 2, 3]


def advanced_func(pos1, pos2, /, normal, *args, kw_only, default=10, **kwargs):
    print(f"位置参数: {pos1}, {pos2}")
    print(f"普通参数: {normal}")
    print(f"可变位置参数: {args}")
    print(f"仅限关键字参数: {kw_only}")
    print(f"默认参数: {default}")
    print(f"可变关键字参数: {kwargs}")

advanced_func(1, 2, 3, 4, 5, kw_only=6, default=7, extra1=8, extra2=9)