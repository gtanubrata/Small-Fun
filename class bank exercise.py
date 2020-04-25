# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def getBalance(self):
        return self.balance
    def deposit(self, credit):
        self.balance += credit
        return self.balance
    def withdraw(self, debit):
        self.balance -= debit
        return self.balance

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print(acct.balance)