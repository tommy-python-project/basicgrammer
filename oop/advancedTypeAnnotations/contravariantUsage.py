"""
逆变实际应用场景

事件处理系统（逆变典型应用）
"""
from typing import TypeVar, Generic, Callable, List


class Event:
    pass

class MouseEvent(Event):
    def handle_click(self) -> str:
        return "鼠标点击处理"

class KeyboardEvent(Event):
    def handle_click(self) -> str:
        return "键盘按下处理"


E = TypeVar('E', bound = Event, contravariant=True)

class EventHandler(Generic[E]):

    def __init__(self, callback: Callable[[E], None]) -> None:
        self._callback = callback

    def handle(self,event: E) -> None:
        self._callback(event)

class EventDispatcher:
    def __init__(self) -> None:
        self._handlers: List[EventHandler[Event]] = []

    def add_handler(self, handler: EventHandler[Event]) -> None:
        self._handlers.append(handler)

    def dispatch(self, event: Event) -> None:
        for handler in self._handlers:
            handler.handle(event)

# 使用示例
def generic_event_handler(event: Event) -> None:
    print("处理通用事件")

def mouse_event_handler(event: MouseEvent) -> None:
    print(f"处理鼠标事件: {event.handle_click()}")

# 创建处理器
generic_handler = EventHandler(generic_event_handler)
mouse_handler = EventHandler(mouse_event_handler)


dispatcher = EventDispatcher()
dispatcher.add_handler(generic_handler)
dispatcher.add_handler(mouse_handler) # 合法 - 逆变！

# 分发事件
dispatcher.dispatch(MouseEvent())

