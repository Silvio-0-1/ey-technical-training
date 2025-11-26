# Create a BankAccount class with deposit and withdraw methods.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Current balance: {self.balance}")
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Current balance: {self.balance}")
        
BA = BankAccount(10000)
BA.deposit(int(input("Enter deposit amount: ")))
BA.withdraw(int(input("Enterwithdraw amount: ")))
