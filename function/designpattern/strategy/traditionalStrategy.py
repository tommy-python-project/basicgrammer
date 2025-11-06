"""
传统的策略模式
"""
from abc import ABC, abstractmethod


class Order:
    """订单类"""
    def __init__(self, price: float, customer_points:int):
        self.price = price
        self.customer_points = customer_points

# 1. 策略接口(ABC)
class Promotion(ABC):
    @abstractmethod
    def apply_discount(self,order: Order) -> float:
        """计算折扣后的价格"""

# 2. 具体策略类
class FullReduction(Promotion):
    def apply_discount(self,order: Order) -> float:
        """满200 减 10"""
        return order.price - 10 if order.price >= 200 else order.price

class PercentageDiscount(Promotion):
    """打 7 折"""
    def apply_discount(self,order: Order) -> float:
        return order.price * 0.7

class CustomerPointsDiscount(Promotion):
    """积分 1000 以上打 8 折"""
    def apply_discount(self,order: Order) -> float:
        return order.price * 0.8 if order.customer_points >= 1000 else order.price

# 3. 上下文（Context）,它使用策略
class OrderContext:

    def __init__(self, order: Order,promotion: Promotion):
        self.order = order
        self.promotion = promotion

    def get_final_price(self) -> float:
        return self.promotion.apply_discount(self.order)

# 使用
order = Order(300,1200)

# 使用策略1
promo1 = FullReduction()
context1 = OrderContext(order, promo1)
print(f"满减价：{context1.get_final_price()}")

# 使用策略3
promo3 = CustomerPointsDiscount()
context3 = OrderContext(order, promo3)
print(f"积分价: {context3.get_final_price()}") # 积分价: 240.0




