class User:
    def __init__(self,name,email,account_balance=0):
        self.name=name
        self.email=email
        self.account_balance=account_balance

    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name,self.account_balance)

    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

Mohammed = User("Mohammed Eleyan","1142456@student.birzeit.edu")
Rashid = User("Rashid Eleyan","1142456@student.birzeit.edu")
Ahmed = User("Ahmed Eleyan","1142456@student.birzeit.edu")


Mohammed.make_deposit(1500)
Mohammed.make_deposit(1100)
Mohammed.make_deposit(1000)
Mohammed.make_withdrawal(700)
Rashid.make_deposit(1200)
Rashid.make_deposit(1400)
Rashid.make_withdrawal(500)
Rashid.make_withdrawal(400)
Ahmed.make_deposit(1700)
Ahmed.make_withdrawal(700)
Ahmed.make_withdrawal(200)
Ahmed.make_withdrawal(300)

Mohammed.transfer_money(Ahmed,500)

Mohammed.display_user_balance()
Rashid.display_user_balance()
Ahmed.display_user_balance()