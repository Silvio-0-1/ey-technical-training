# Example 1: BankAccount → SavingsAccount

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"[BankAccount] Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("[BankAccount] Insufficient funds!")
            return False
        self.balance -= amount
        print(f"[BankAccount] Withdrew {amount}. New balance: {self.balance}")
        return True


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.04):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"[SavingsAccount] Interest {interest} added. Balance: {self.balance}")


sa = SavingsAccount("Shubham", 1000)
sa.deposit(500)
sa.add_interest()
sa.withdraw(300)


# Example 2: User → AdminUser

class User:
    def __init__(self, username):
        self.username = username
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        print(f"[User] {self.username} deactivated.")

    def info(self):
        return {"username": self.username, "is_active": self.is_active}


class AdminUser(User):
    def __init__(self, username):
        super().__init__(username)
        self.role = "admin"

    def reset_password(self, target_user):
        print(f"[AdminUser] {self.username} reset password for {target_user.username}.")

    def info(self):
        base = super().info()
        base["role"] = self.role
        return base


u = User("alice")
admin = AdminUser("admin_shubham")
print(admin.info())
admin.reset_password(u)
u.deactivate()
