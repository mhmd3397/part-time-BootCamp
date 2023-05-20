class User:
    def __init__(self,name,email,account_balance=0):
        self.name=name
        self.email=email
        self.account_balance=account_balance

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name,self.account_balance)

    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

Mohammed = User("Mohammed Eleyan","1142456@student.birzeit.edu")
Rashid = User("Rashid Eleyan","1142456@student.birzeit.edu")
Ahmed = User("Ahmed Eleyan","1142456@student.birzeit.edu")

Mohammed.make_deposit(1500).make_deposit(1100).make_deposit(1000).make_withdrawal(700).transfer_money(Ahmed,500).display_user_balance()
Rashid.make_deposit(1200).make_deposit(1400).make_withdrawal(500).make_withdrawal(400).display_user_balance()
Ahmed.make_deposit(1700).make_withdrawal(700).make_withdrawal(200).make_withdrawal(300).display_user_balance()