# Parent class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


# Child class 1: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest added:", interest)


# Child class 2: CurrentAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(amount, "withdrawn using overdraft facility.")
        else:
            print("Overdraft limit exceeded.")


# Creating objects and testing methods

print("---- Savings Account ----")
sa = SavingsAccount("Tauseer", 10000, 5)
sa.display_balance()
sa.deposit(2000)
sa.add_interest()
sa.withdraw(3000)
sa.display_balance()

print("\n---- Current Account ----")
ca = CurrentAccount("Rahul", 5000, 3000)
ca.display_balance()
ca.deposit(1000)
ca.withdraw_with_overdraft(7000)
ca.display_balance()
