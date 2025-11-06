"""
接口兼容性和属性隐藏
"""
class BankAccount:

    def __init__(self,balance = 0):
        self._balance = balance
        self._transaction_count = 0

    @property
    def balance(self):
        """余额是只读的，不能直接修改"""
        return self._balance

    def deposit(self,amount):
        """存款"""
        if amount < 0:
            raise ValueError("存款金额必须大于0")
        self._balance += amount
        self._transaction_count += 1

    def withdraw(self,amount):
        """取款"""
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount
        self._transaction_count += 1

    @property
    def transaction_count(self):
        """交易次数 - 只读"""
        return self._transaction_count

    @property
    def can_withdraw(self):
        """是否可以取款 - 计算属性"""
        return self._balance > 0

# 使用示例
account = BankAccount(1000)
print(f"余额：{account.balance}")
print(f"可以取款：{account.can_withdraw}")

account.deposit(500)
account.withdraw(200)
print(f"余额：{account.balance}")
print(f"交易次数：{account.transaction_count}")

account.balance = 2000 # 报错！余额是只读的
