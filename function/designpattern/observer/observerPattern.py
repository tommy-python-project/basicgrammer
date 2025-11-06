class Event:
    """事件类"""
    def __init__(self):
        self._subscribers = []

    def subscribe(self, callback):
        """订阅事件"""
        self._subscribers.append(callback)

    def unsubscribe(self, callback):
        """取消订阅"""
        self._subscribers.remove(callback)

    def notify(self, *args, **kwargs):
        """通知所有订阅者"""
        for callback in self._subscribers:
            callback(*args, **kwargs)

# 使用示例
class Button:
    def __init__(self):
        self.click_event = Event()
        self.double_click_event = Event()

    def click(self):
        print("按钮被点击")
        self.click_event.notify("单击事件")

    def double_click(self):
        print("按钮被双击")
        self.double_click_event.notify("双击事件")

# 创建事件处理器
def log_click(message):
    print(f"日志: {message}")

def update_ui(message):
    print(f"UI更新: {message}")

def send_analytics(message):
    print(f"发送分析: {message}")

# 使用
button = Button()

# 订阅事件
button.click_event.subscribe(log_click)
button.click_event.subscribe(update_ui)
button.double_click_event.subscribe(send_analytics)

# 触发事件
button.click()
button.double_click()