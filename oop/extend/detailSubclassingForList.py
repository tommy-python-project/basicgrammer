from collections import UserList

def print_sep(title):
    print(f"\n{'=' * 20} {title} {'=' * 20}")

class MyList(list):
    def __init__(self, *args):

        super().__init__(*args)
        print(f"[MyList.__init__] 初始化 {self}")

    def append(self, item):
        print(f"[MyList.append] ✅ 子类方法执行 append({item!r})")
        super().append(item)

    def insert(self, index, item):
        print(f"[MyList.insert] ✅ 子类方法执行 insert({index}, {item!r})")
        super().insert(index, item)

    def __setitem__(self, index, value):
        print(f"[MyList.__setitem__] ✅ 子类方法执行 __setitem__({index}, {value!r})")
        super().__setitem__(index, value)

    def extend(self, iterable):
        print(f"[MyList.extend] ✅ 子类方法执行 extend({list(iterable)!r})")
        super().extend(iterable)

    def __iadd__(self, other):
        print(f"[MyList.__iadd__] ✅ 子类方法执行 __iadd__({list(other)!r})")
        return super().__iadd__(other)


class MyUserList(UserList):
    def append(self, item):
        print(f"[MyUserList.append] ✅ 子类方法执行 append({item!r})")
        super().append(item)

    def insert(self, index, item):
        print(f"[MyUserList.insert] ✅ 子类方法执行 insert({index}, {item!r})")
        super().insert(index, item)

    def __setitem__(self, index, value):
        print(f"[MyUserList.__setitem__] ✅ 子类方法执行 __setitem__({index}, {value!r})")
        super().__setitem__(index, value)

    def extend(self, iterable):
        print(f"[MyUserList.extend] ✅ 子类方法执行 extend({list(iterable)!r})")
        super().extend(iterable)

    def __iadd__(self, other):
        print(f"[MyUserList.__iadd__] ✅ 子类方法执行 __iadd__({list(other)!r})")
        return super().__iadd__(other)


def test_list_class(cls):
    print_sep(f"测试 {cls.__name__}")
    lst = cls([1, 2, 3])
    print(f"-- 初始值: {lst}")

    print("执行 append(99)")
    lst.append(99)

    print("执行 insert(0, -1)")
    lst.insert(0, -1)

    print("执行 lst[1] = 42")
    lst[1] = 42

    print("执行 extend([7, 8])")
    lst.extend([7, 8])

    print("执行 += [10, 11]")
    lst += [10, 11]

    print("最终结果:", lst)
    return lst


if __name__ == "__main__":
    print("=== 对比实验：内置 list 子类 vs UserList 子类 ===")
    test_list_class(MyList)
    test_list_class(MyUserList)
