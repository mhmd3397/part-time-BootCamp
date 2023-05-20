'''
This module is for assignment Users with Bank Accounts in Coding Dojo
Mohammed Eleyan
18-05-2023
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

class User:
    def __init__(self, name, email, int_rate, account_balance):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate, account_balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self


mohammed = User("Mohammed Eleyan", "1142456@student.birzeit.edu", 0.02, 100)
rashid = User("Rashid Eleyan", "1142456@student.birzeit.edu", 0.04, 50)
ahmed = User("Ahmed Eleyan", "1142456@student.birzeit.edu", 0.06, 150)

mohammed.make_deposit(1500).make_deposit(1100).make_deposit(1000).make_withdrawal(
    700).transfer_money(ahmed, 500).yield_interest().display_user_balance()
rashid.make_deposit(1200).make_deposit(1400).make_withdrawal(
    500).make_withdrawal(400).yield_interest().display_user_balance()
ahmed.make_deposit(1700).make_withdrawal(700).make_withdrawal(
    200).make_withdrawal(300).yield_interest().display_user_balance()
