import math


def dirTest():
    # print(dir(math))  # 查看math模块的所有内容
    #
    # # 只查看不以__开头的方法（过滤掉魔术方法）
    # methods = [method for method in dir(math) if not method.startswith('__')]
    # print(methods)
    #
    # # 查看对象的属性和方法
    # my_list = [1, 2, 3]
    # print(dir(my_list))  # 查看列表的所有方法
    #
    # # 查看类的属性和方法
    # print(dir(str))  # 查看字符串类的方法
    #
    #
    # my_list = [1, 2, 3]
    # print('append' in dir(my_list))  # True
    # print('sort' in dir(my_list))    # True


    # 查看函数的帮助
    help(print)

    # 查看方法的帮助
    my_list = [1, 2, 3]
    help(my_list.append)

    # 查看模块的帮助
    import math
    help(math)

if __name__ == '__main__':
    dirTest()