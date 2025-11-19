"""
使用抽象基类显示表示接口
"""
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """支付处理器抽象接口"""

    @abstractmethod
    def process_payment(self, amount):
        """处理支付"""
        pass

    @abstractmethod
    def refund_payment(self, amount):
       """退款处理"""
       pass

    def validate_amount(self, amount):
        """验证金额（提供默认实现）"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return True

class ReportGenerator(ABC):
    """报告生成器抽象接口"""

    @abstractmethod
    def generate_report(self):
        """生成报告"""
        pass

    def export_report(self,format_type="pdf"):
        """导出报告（提供默认实现）"""
        report = self.generate_report()
        return f"Exporting {format_type} report: {report}"

# 具体实现
class CreditCardProcessor(PaymentProcessor):

    def process_payment(self, amount):
        self.validate_amount(amount)
        return f"Processing credit card payment: ${amount}"

    def refund_payment(self, amount):
        self.validate_amount(amount)
        return f"Refunding credit card payment: ${amount}"

class SalesReport(ReportGenerator):
    def generate_report(self):
        return "Monthly Sales Report Data"

# 多重接口实现
class CompletePaymentSystem(PaymentProcessor,ReportGenerator):
    """完整的支付系统，实现多个接口"""

    def process_payment(self, amount):
        self.validate_amount(amount)
        return f"Complete system processing: ${amount}"

    def refund_payment(self, amount):
        self.validate_amount(amount)
        return f"Complete system refunding: ${amount}"

    def generate_report(self):
        return "Complete System Transaction Report"

# 使用
processors = [
    CreditCardProcessor(),
    CompletePaymentSystem()
]

for processor in processors:
    print(processor.process_payment(100))
    if isinstance(processor, ReportGenerator):
        print(processor.generate_report())