'''
This module is for assignment Bankaccount  in Coding Dojo
'''


class BankAccount:
    def __init__(self, int_rate=0.16, balance=-0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self
        elif amount > self.balance:
            self.balance -= 5
            print('Insufficient funds: Charging a $5 fee')
            return self

    def display_account_info(self):
        print(f"int_rate: ${self.int_rate} Balance: ${self.balance} ")

    def yield_interest(self):
        self.balance = self.balance+(self.balance * self.int_rate)
        return self


mohammad_account = BankAccount(balance=500)
ahmad_account = BankAccount(0.05, 50)

mohammad_account.deposit(50).deposit(200).deposit(
    300).withdraw(250).yield_interest().display_account_info()

ahmad_account.deposit(100).deposit(100).withdraw(125).withdraw(25).withdraw(
    50).withdraw(100).yield_interest().display_account_info()
