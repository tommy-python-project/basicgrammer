"""
仅子类化为拓展而设计的类
"""

# 设计用于拓展的基类
class ExtensibleBase:
    """设计用于被继承的基类"""

    def __init__(self):
        self.hooks = []

    def add_hook(self,hook_function):
        """添加狗子函数，允许拓展"""
        self.hooks.append(hook_function)


    def execute_with_hook(self,main_function,*args,**kwargs):
        """执行主函数前后调用钩子"""
        # 前置钩子
        for hook in self.hooks:
            hook('before',*args,**kwargs)

        # 主逻辑
        result = main_function(*args,**kwargs)

        # 后置钩子
        for hook in self.hooks:
            hook('after',*args,**kwargs)

        return result

    def template_method(self):
        """模版方法，定义算法骨架"""
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        """可重写的步骤1"""
        print("Base step1")

    def step2(self):
        """可重写的步骤2"""
        print("Base step2")

    def step3(self):
        """可重写的步骤3"""
        print("Base step3")


# 正确拓展
class CustomImplementation(ExtensibleBase):
    def step2(self):
        """重写步骤2"""
        print("Custom step2")

    def step3(self):
        """重写步骤3"""
        print("Custom step3")

    def custom_operation(self,data):
        def main_logic(data):
            print(f"Processing: {data}")
            return f"Processed: {data}"

        return self.execute_with_hook(main_logic,data)


# 使用
custom = CustomImplementation()

# 添加钩子
custom.add_hook(lambda phase, *args: print(f"Hook: {phase} with {args}"))

# 执行操作
result = custom.custom_operation("test data")
print("Result:", result)

# 执行模板方法
print("\nTemplate method execution:")
custom.template_method()
