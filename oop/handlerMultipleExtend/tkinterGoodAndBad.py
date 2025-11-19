"""
分析 Tkinter 中多重继承的使用
"""
import tkinter as tk
from tkinter import ttk, messagebox


# Tkinter 的良好实践示例
class BaseFrame(ttk.Frame):
    """基础框架，提供通用功能"""

    def __init__(self, parent,title="",**kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.title = title
        self.create_widgets()
        self.setup_layout()
        self.bind_events()


    def create_widgets(self):
        """创建控件 （由子类实现）"""
        pass

    def setup_layout(self):
        """设置布局（由子类实现）"""
        pass

    def bind_events(self):
        """绑定事件（由子类实现）"""
        pass

class ValidatedMixin:
    """验证功能混合类"""

    def add_validation(self,widget,validation_type):
        """添加验证规则"""

        if validation_type == 'email':
            widget.config(validate='focusout',
                         validatecommand=(self.register(self.validate_email), '%P'))
        elif validation_type == 'number':
            widget.config(validate='key',
                          validatecommand=(self.register(self.validate_number), '%P'))

    def validate_email(self,value):
        """验证邮箱格式"""
        if value == '':
            return True
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, value) is not None

    def validate_number(self,value):
        """验证数字"""
        if value == '' or value.isdigit():
            return True
        return False


class TooltipMixin:
    """工具提示混合类"""

    def create_tooltip(self,widget,text):
        """创建工具提示"""
        def show_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")

            label = tk.Label(tooltip, text=text, background="lightyellow",
                             relief='solid', borderwidth=1)
            label.pack()

            widget.tooltip_window = tooltip

        def hide_tooltip(event):
            if hasattr(widget, 'tooltip_window'):
                widget.tooltip_window.destroy()

        widget.bind('<Enter>', show_tooltip)
        widget.bind('<Leave>', hide_tooltip)


# 良好的多重继承使用
class LoginForm(BaseFrame,ValidatedMixin,TooltipMixin):
    """登录表单，组合多个功能"""

    def create_widgets(self):
        # 用户名
        ttk.Label(self, text="用户名:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.username_entry = ttk.Entry(self, width=20)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # 邮箱
        ttk.Label(self, text="邮箱:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(self, width=20)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        # 按钮
        self.login_button = ttk.Button(self, text="登录", command=self.on_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def setup_layout(self):
        self.grid_columnconfigure(1, weight=1)

    def bind_events(self):
        # 添加验证
        self.add_validation(self.email_entry, 'email')

        # 添加工具提示
        self.create_tooltip(self.username_entry, "请输入您的用户名")
        self.create_tooltip(self.email_entry, "请输入有效的邮箱地址")
        self.create_tooltip(self.login_button, "点击登录系统")

    def on_login(self):
        """登录按钮点击事件"""
        username = self.username_entry.get()
        email = self.email_entry.get()

        if username and email:
            messagebox.showinfo("成功", f"欢迎 {username}!")
        else:
            messagebox.showerror("错误", "请填写所有字段")


# Tkinter 的问题示例（应该避免的）
class BadInheritanceExample(tk.Tk, ttk.Frame):  # 错误：多重继承根窗口和框架
    """不良的多重继承示例"""

    def __init__(self):
        # 这会导致混淆，因为 Tk 和 Frame 都有不同的职责
        tk.Tk.__init__(self)
        ttk.Frame.__init__(self)
        self.title("Bad Example")


# 正确的做法： 使用组合
class GoodApplication:
    """良好的应用结构（使用组合）"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Good Example")
        self.root.geometry("300x200")

        # 创建框架实例
        self.login_frame = LoginForm(self.root)
        self.login_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def run(self):
        """运行应用"""
        self.root.mainloop()

# 使用
if __name__ == "__main__":
    app = GoodApplication()
    app.run()
