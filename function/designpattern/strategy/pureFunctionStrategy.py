"""
纯函数实现策略模式
"""

class Order:
    """订单类，保持不变"""
    def __init__(self, price: float, customer_points: int) -> None:
        self.price = price
        self.customer_points = customer_points



# 1. 直接把策略定义为函数
#    函数的签名 (接受一个 Order，返回一个 float) 保持一致即可
def no_discount(order: Order) -> float:
    return order.price


def full_reduction_promo(order: Order) -> float:
    """满200 减10"""
    return order.price - 10 if order.price >= 200 else order.price

def percentage_promo(order: Order) -> float:
    """打 7 折"""
    return order.price * 0.7

def customer_points_promo(order: Order) -> float:
    """积分 1000 以上打 8 折"""
    return order.price * 0.8 if order.customer_points >= 1000 else order.price

# 2. 修改上下文（Context）
#    它不再需要一个类型提示，或者可以提示为 Callable



class OrderContext:

    def __init__(self, order: Order, discount_strategy= no_discount) :
        self.order = order
        self.promotion = discount_strategy # 持有一个 *函数*

    def get_final_price(self) -> float:
        # 直接调用函数，而不是调用 .apply_discount() 方法
        return self.promotion(self.order)

# --- 使用 ---
order = Order(300,1200)

# 使用策略1 （直接传入函数名）
context1 = OrderContext(order, full_reduction_promo)
print(f"满减价: {context1.get_final_price()}") # 满减价: 290.0

# 使用策略3 （直接传入函数名）
context3 = OrderContext(order, customer_points_promo)
print(f"积分价: {context3.get_final_price()}") # 积分价: 240.0