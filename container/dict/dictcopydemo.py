
"""
字典的拷贝
"""
import copy


def copyTest():

    # 原始字典
    original = {"a":1,"b":2,"c":3}

    # 创建拷贝
    copied = original.copy()

    print(copied)
    print(original)
    print(original is copied)

    # 直接赋值 - 引用同一个对象
    dict1 = {"a":1,"b":2}
    dict2 = dict1 #直接赋值
    dict2["c"] = 3
    print(dict1)
    print(dict2)


    # 使用copy() - 创建新对象
    dict3 = {"a":1,"b":2}
    dict4 = dict3.copy() #牵拷贝
    dict4["c"] = 3
    print(dict3)
    print(dict4)


def simpleCopyLimitTest():
    """
    浅拷贝的局限性：浅拷贝只拷贝第一层，嵌套对象仍然是引用：
    """
    print("========================")
    original = {
        "name":"Alice",
        "scores":{"math":90,"english":85},
        "hobbies": ["reading","swimming"]
    }

    copied = original.copy()

    # 修改第一层 -- 不影响原字典
    copied["name"] = "Bob"
    print(original["name"])  # 'Alice' --不受影响

    # 修改嵌套对象 -- 会影响原字典
    copied["scores"]["math"] = 100
    copied["hobbies"].append("running")


    print(original["scores"]["math"])  # 100 - 被修改了
    print(original["hobbies"])    # ['reading', 'swimming', 'running'] - 被修改了！

def deepCopyTest():
    print("==========deepcopy==============")

    original = {
        "name":"Alice",
        "scores":{"math":90,"english":85},
        "hobbies": ["reading","swimming"]
    }

    # 深拷贝
    deep_copied = copy.deepcopy(original)

    # 现在修改嵌套对象不会影响原字典
    deep_copied['scores']['math'] = 100
    deep_copied['hobbies'].append('running')

    print(original['scores']['math'])  # 90 - 保持不变
    print(original['hobbies'])  # ['reading', 'swimming'] - 保持不变

    name1 = "Tom"
    name2 = "Tom"
    print(id(name1))
    print(id(name2))
    name1 = "Jerry"
    print(id(name1))
    print(id(name2))


if __name__ == "__main__":
    copyTest()
    simpleCopyLimitTest()
    deepCopyTest()