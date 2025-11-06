"""
用函数实现命令模式
"""

class Light:

    def turn_on(self):
        print("灯亮了")

    def turn_off(self):
        print("灯灭了")

# 命令作为函数
def create_light_on_command(light):
    def command():
        light.turn_on()
    return command

def create_light_off_command(light):
    def command():
        light.turn_off()
    return command

# 或者更简单，直接使用方法引用
light = Light()
on_command = light.turn_on
off_command = light.turn_off

# 命令调用
on_command()  # 输出: 灯亮了
off_command() # 输出: 灯灭了

# 命令队列
class CommandQueue:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_all(self):
        for command in self.commands:
            command()
        self.commands.clear()

# 使用命令队列
queue = CommandQueue()
queue.add_command(light.turn_on)
queue.add_command(light.turn_off)
queue.execute_all()