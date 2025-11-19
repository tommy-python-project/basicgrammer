"""
Tkinter 中的多重继承
"""

import tkinter as tk
from tkinter import ttk, messagebox


class TooltipMixin:
    """为控件添加工具提示的混合类"""

    def create_tooltip(self, widget, text):
        """创建工具提示"""

        def on_enter(event):
            x, y, _, _ = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 25

            # 创建工具提示窗口
            self.tooltip = tk.Toplevel(widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")

            label = tk.Label(self.tooltip, text=text, justify='left',
                             background="#ffffe0", relief='solid', borderwidth=1)
            label.pack()

        def on_leave(event):
            if hasattr(self, 'tooltip'):
                self.tooltip.destroy()

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)


class ValidationMixin:
    """输入验证混合类"""

    def add_number_validation(self, widget):
        """添加数字验证"""
        vcmd = (self.register(self.validate_number), '%P')
        widget.config(validate='key', validatecommand=vcmd)

    def validate_number(self, value):
        """验证输入是否为数字"""
        if value == "" or value.isdigit():
            return True
        return False


class AutoSaveMixin:
    """自动保存混合类"""

    def enable_auto_save(self, callback, interval=5000):
        """启用自动保存"""
        self.auto_save_callback = callback
        self.auto_save_interval = interval
        self.after(interval, self.auto_save)

    def auto_save(self):
        """自动保存"""
        if hasattr(self, 'auto_save_callback'):
            self.auto_save_callback()
        self.after(self.auto_save_interval, self.auto_save)


# 组合所有功能的应用程序类
class AdvancedApplication(TooltipMixin, ValidationMixin, AutoSaveMixin, tk.Tk):
    """具有高级功能的 Tkinter 应用程序"""

    def __init__(self):
        super().__init__()
        self.title("多重继承示例")
        self.geometry("400x300")

        self.create_widgets()
        self.setup_validation()
        self.setup_tooltips()
        self.setup_auto_save()

    def create_widgets(self):
        """创建界面控件"""
        # 输入框架
        input_frame = ttk.Frame(self, padding="10")
        input_frame.pack(fill=tk.X)

        ttk.Label(input_frame, text="姓名:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="年龄:").grid(row=1, column=0, sticky=tk.W)
        self.age_entry = ttk.Entry(input_frame, width=30)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        # 按钮框架
        button_frame = ttk.Frame(self, padding="10")
        button_frame.pack(fill=tk.X)

        self.save_button = ttk.Button(button_frame, text="保存", command=self.save_data)
        self.save_button.pack(side=tk.LEFT, padx=5)

        ttk.Button(button_frame, text="清除", command=self.clear_data).pack(side=tk.LEFT, padx=5)

    def setup_validation(self):
        """设置验证"""
        self.add_number_validation(self.age_entry)

    def setup_tooltips(self):
        """设置工具提示"""
        self.create_tooltip(self.name_entry, "请输入您的全名")
        self.create_tooltip(self.age_entry, "请输入数字年龄")
        self.create_tooltip(self.save_button, "保存当前数据")

    def setup_auto_save(self):
        """设置自动保存"""
        self.enable_auto_save(self.auto_save_data)

    def save_data(self):
        """保存数据"""
        name = self.name_entry.get()
        age = self.age_entry.get()

        if name and age:
            messagebox.showinfo("成功", f"数据已保存:\n姓名: {name}\n年龄: {age}")
        else:
            messagebox.showwarning("警告", "请填写所有字段")

    def auto_save_data(self):
        """自动保存数据（模拟）"""
        name = self.name_entry.get()
        age = self.age_entry.get()

        if name or age:
            print(f"自动保存: 姓名={name}, 年龄={age}")

    def clear_data(self):
        """清除数据"""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)


# 使用示例
if __name__ == "__main__":
    app = AdvancedApplication()
    app.mainloop()
