"""
match - 模式匹配
"""

def process_command(command):
    match command:
        case ["start",service]:
            # 匹配列表["start", 任何值]，并捕获第二个值到 service
            print(f"✅ 启动服务: {service}")
        case ["stop",service]:
            print(f"🛑 停止服务: {service}")
        case ["status"]:
            # 匹配字面量列表 ["status"]
            print("ℹ️ 获取系统状态...")
        case ["log", *rest]:
            # 匹配以 "log" 开头的列表，并捕获其余元素到 rest
            print(f"📜 查看日志，参数: {rest}")
        case ["reboot", delay] if delay > 60:
            # 匹配 ["reboot", 任何大于 60 的值]，并使用卫语句
            print(f"⏳ 延迟 {delay} 秒后重启...")
        case _:
            # 通配符，匹配所有其他情况
            print(f"❌ 未知命令: {command}")

# 示例调用
process_command(["start", "web_server"])
process_command(["status"])
process_command(["log", "level=debug", "lines=100"])
process_command(["reboot", 300])
process_command(["reboot", 30]) # 匹配到 _
process_command("help")


print("====复杂模式匹配======")

# 1. 匹配元组/列表
def handle_point(point):
    match point:
        case (0,0):
            print("原点")
        case (x,0):
            print(f"X轴上的点: ({x}, 0)")
        case(0,y):
            print(f"Y轴上的点: (0, {y})")
        case (x, y):
            print(f"普通点: ({x}, {y})")
        case _:
            print("不是二维点")

handle_point((0, 0))    # 原点
handle_point((5, 0))    # X轴上的点: (5, 0)
handle_point((3, 4))    # 普通点: (3, 4)

# 2. 匹配带类型的模式
def process_data(data):
    match data:
        case int() | float() as num if num > 0:
            return f"正数: {num}"
        case list() as lst if len(lst) > 0:
            return f"非空列表: {lst}"
        case str() as s if s.startswith("http"):
            return f"URL: {s}"
        case _:
            return "其他类型"

print(process_data(42))            # 正数: 42
print(process_data([1, 2, 3]))     # 非空列表: [1, 2, 3]
print(process_data("http://example.com"))  # URL: http://example.com