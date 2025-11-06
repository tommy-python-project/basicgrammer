
def test():
    d = dict()

    d["明世隐"] = "小明"  # 使用较多的方式
    d.setdefault("诸葛亮", "孔明")  # 一次只能增加一个键值对数据
    d.update({"鬼谷子":"老鬼", "花木兰": "小兰"})  # 一次增加多个键值对数据
    print(d)

    d["明世隐"] = "小明"
    d.update({"鬼谷子": "小姑"})  # key存在的情况下会修改数据，key不存在就插入
    d.setdefault("花木兰","花花") # key存在，什么都不做
    print(d)

    d.pop("花木兰")  # 使用较多的操作
    print(d)
    d.popitem()  # 随机删除一个
    print(d)

    # 遍历
    for key in d.keys():
        print("key:",key,", value:", d.get(key))
    print("-----------------")

    for key,value in d.items():
        print("key:",key,", value:", value)


if __name__ == "__main__":
    test()