def reassign_list(lst):
    lst = [10, 20, 30]  # 创建新的局部变量，不影响外部
    print(f"函数内部: {lst}")

def safe_modify(lst):
    lst_copy = lst.copy()  # 创建副本
    lst_copy.append(4)
    print(f"函数内部副本: {lst_copy}")

if __name__ == "__main__":
    # my_list = [1, 2, 3]
    # reassign_list(my_list)
    # print(f"函数外部: {my_list}")  # 还是 [1, 2, 3]

    # 传递副本#
    my_list = [1, 2, 3]
    safe_modify(my_list.copy())  # 传递副本
    # 或者 safe_modify(my_list[:])  # 切片也是副本
    print(f"函数外部原列表: {my_list}")  # 保持 [1, 2, 3]