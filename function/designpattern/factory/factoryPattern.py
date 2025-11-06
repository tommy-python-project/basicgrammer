"""
工厂模式
用函数实现工厂模式
"""

# 产品函数
def create_email_notifier():
    def notify(message):
        print(f"发送邮件：{message}")
    return notify

def create_sms_notifier():
    def notify(message):
        print(f"发送短信: {message}")
    return notify

def create_push_notifier():
    def notify(message):
        print(f"发送推送: {message}")
    return notify

# 工厂函数
def create_notifier(notifier_type):
    notifiers = {
        "email": create_email_notifier,
        "sms": create_sms_notifier,
        "push": create_push_notifier,
    }

    creator = notifiers.get(notifier_type)
    if creator:
        return creator()
    else:
        raise ValueError(f"未知的通知类型: {notifier_type}")
    
# 使用工厂
email_notifier = create_notifier('email')
sms_notifier = create_notifier('sms')

email_notifier("您的订单已发货")
sms_notifier("验证码: 123456")