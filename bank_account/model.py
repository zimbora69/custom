class BankAccount(object):
    balance = 0
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "This bank account belongs to %s it has a balance of R$ %.2f" % (self.name, self.balance)

    def show_balance(self):
        return "Balance of your account is R$ %2.f" % (self.balance)

    def deposit(self,amount):
        self.amount = amount
        if amount <= 0:
            print "Deposit amount is invalid!"
            return
        else:
            print "Amount deposited is R$ %2.f" % (self.amount)
            self.balance += amount
            self.show_balance()

    def withdraw(self,amount):
        self.amount = amount
        if amount > self.balance:
            print "Your withdraw amount is greater than your balance"
            return
        else:
            print "You are withdrawing R$ %2.f" % (self.amount)
            self.balance -= amount
            self.show_balance()

"""
        ### EXEMPLO ###
my_account = BankAccount("Alexandre")
print my_account
my_account.deposit(2000)
print my_account.show_balance()
my_account.withdraw(1000)
print my_account.show_balance()
print my_account
my_account.withdraw(1001)

"""

