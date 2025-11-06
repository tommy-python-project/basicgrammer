import sys


def add(x, y=10):
    return x + y

def func_a():
    print("func_a 开始")
    func_b()
    print("func_a 结束")

def func_b():
    print("func_b 开始")
    func_c()
    print("func_b 结束")

def func_c():
    print("func_c 执行")


def show_frame_info(x, y):
    local_var = x + y
    frame = sys._getframe()

    print("局部变量:", frame.f_locals)
    print("函数名:", frame.f_code.co_name)
    print("行号:", frame.f_lineno)

if __name__ == "__main__":
    # print(add.__name__)  # 'add'
    # print(add.__defaults__)  # (10,)
    # print(add.__code__.co_varnames)  # ('x', 'y')
    #func_a()

    show_frame_info(10, 20)