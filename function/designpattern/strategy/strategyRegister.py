"""
策略注册表
"""



class Order:
    """订单类"""
    def __init__(self, price: float, customer_points: int) -> None:
        self.price = price
        self.customer_points = customer_points

class DiscountStrategyRegistry:
    """折扣策略注册表"""
    _strategies = {}


    @classmethod
    def register(cls, name: str) :
        """注册策略的装饰器"""
        def decorator(func) :
            # 验证函数签名
            if not callable(func):
                raise ValueError(f"策略 '{name}' 必须是一个可调用对象")

            # 简单验证函数参数 (可选，但推荐)
            try:
                # 创建一个测试订单来验证函数是否能正常处理
                test_order = Order(100.0,500)
                result = func(test_order)
                if not isinstance(result, (int, float)):
                    print(f"警告: 策略 '{name}' 返回了非数值类型: {type(result)}")
            except Exception as e:
                raise ValueError(f"策略 '{name}' 验证失败: {e}") from e

            cls._strategies[name] = func
            return func
        return decorator

    @classmethod
    def get_strategy(cls, name: str) :
        """获取策略函数"""
        if name not in cls._strategies:
            available_strategies = list(cls._strategies.keys())
            raise ValueError(
                f"未知的折扣策略: '{name}'。可用策略: {available_strategies}"
            )
        return cls._strategies[name]

    @classmethod
    def list_strategies(cls):
        """列出所有可用策略"""
        return list(cls._strategies.keys())

    @classmethod
    def strategy_exists(cls, name: str) -> bool:
        """检查策略是否存在"""
        return name in cls._strategies

@DiscountStrategyRegistry.register("no_discount")
def no_discount(order: Order) -> float:
    return order.price

@DiscountStrategyRegistry.register("full_reduction")
def full_reduction(order: Order) -> float:
    """满200 减10"""
    return order.price - 10 if order.price >= 200 else order.price

@DiscountStrategyRegistry.register("percentage")
def percentage(order: Order) -> float:
    """打 7 折"""
    return order.price * 0.7

@DiscountStrategyRegistry.register("customer_points")
def customer_points(order: Order) -> float:
    """积分 1000 以上打 8 折"""
    return order.price * 0.8 if order.customer_points >= 1000 else order.price

@DiscountStrategyRegistry.register("composite")
def composite_promo(order: Order) -> float:
    """组合策略：先满减，再积分折扣"""
    price_after_full_reduction = full_reduction(order)
    temp_order = Order(price_after_full_reduction, order.customer_points)
    return customer_points(temp_order)


class OrderContext:

    def __init__(self, order: Order, discount_strategy_name: str = "no_discount") :
        self.promotion = None
        self.order = order
        self._strategy_name = None
        self.set_discount_strategy(discount_strategy_name)

    def set_discount_strategy(self, strategy_name: str) :
        """通过策略名称设置折扣策略"""
        self.promotion = DiscountStrategyRegistry.get_strategy(strategy_name)
        self._strategy_name = strategy_name

    def get_final_price(self) -> float :
        """获取最终价格"""
        return self.promotion(self.order)

    def get_strategy_name(self) -> str:
        """获取当前策略名称"""
        return self._strategy_name

    def get_available_strategies(self):
        """获取所有可用策略列表"""
        return DiscountStrategyRegistry.list_strategies()

    def describe_discount(self) -> str:
        """描述当前应用的折扣"""
        original_price = self.order.price
        final_price = self.get_final_price()
        discount_amount = original_price - final_price
        discount_percentage = (discount_amount / original_price) * 100 if original_price > 0 else 0

        return (f"原价: {original_price}, "
                f"最终价: {final_price:.2f}, "
                f"节省: {discount_amount:.2f} ({discount_percentage:.1f}%)")



# ---使用示例 ---
def main():
    # 创建订单
    order =Order(300.0, 1200)

    print("=== 策略模式注册表示例 ===")
    print(f"可用策略: {DiscountStrategyRegistry.list_strategies()}")
    print()

    # 使用不同的策略
    strategies_to_test = [
        "no_discount",
        "full_reduction",
        "percentage",
        "customer_points",
        "composite"
    ]

    for strategy_name in strategies_to_test:
        context = OrderContext(order, strategy_name)
        final_price = context.get_final_price()
        description = context.describe_discount()

        print(f"策略 '{strategy_name}':")
        print(f"描述:  {description}")
        print(f"价格:  {final_price}")
        print()

    # 演示动态切换策略
    print("=== 动态切换策略 ===")
    context = OrderContext(order, "no_discount")
    print(f"初始策略: {context.get_strategy_name()}, 价格: {context.get_final_price()}")

    # 切换到满减策略
    context.set_discount_strategy("full_reduction")
    print(f"切换后策略: {context.get_strategy_name()}, 价格: {context.get_final_price()}")

    # 切换到组合策略
    context.set_discount_strategy("composite")
    print(f"最终策略: {context.get_strategy_name()}, 价格: {context.get_final_price()}")

    # 错误处理示例
    print("\n=== 错误处理示例 ===")
    try:
        context.set_discount_strategy("invalid_strategy")
    except ValueError as e:
        print(f"错误信息: {e}")

if __name__ == "__main__":
    main()