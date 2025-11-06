"""
封装
"""
from os import access


class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.__balance = balance # 私有属性(双下划线)

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            return f"存款成功，当前余额：{self.__balance}"
        return None

    def withdraw(self,amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            return f"取款成功，当前余额：{self.__balance}"
        return "余额不足"

    def get_balance(self):
        return self.__balance

account = BankAccount("张三",1000)
print(account.deposit(500))
print(account.get_balance())
