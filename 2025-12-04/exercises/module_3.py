# MODULE 3: Classes, OOPs, Inheritance, Overriding (8 Exercises)

# 16. Build a Student class storing id, name, and marks. Add methods to calculate grade.
class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        return "A" if self.marks > 80 else "B" if self.marks > 60 else "C"

s = Student(101, "Ethan", 81)
print(s.calculate_grade())


# 17. Implement a Product —> ElectronicProduct (inheritance) where Electronics adds warranty years.
class Product:
    def __init__(self, name,):
        self.name = name

class ElectronicProduct(Product):
    def __init__(self, name, warranty):
        super().__init__(name)
        self.warranty = warranty

PowerBank = ElectronicProduct("Power Bank", 2)
print("Product Name: ", PowerBank.name)
print("Warranty: ", PowerBank.warranty, " years")


# 18. Create a Payment class subclasses overriding process-payment().
class Amazon():
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount


class AmazonPayBalance(Amazon):
    def __init__(self, balance, amount, phone_number):
        super().__init__(balance, amount)
        self.phone_number = phone_number

    def payment(self):
        password = input("Enter Your Amazon Password: ")
        if self.amount > self.balance:
            print("Insufficient Amazon Pay Balance!")
            return
        print("\nPayment is successful!")
        print("Remaining Amazon Pay Balance:", self.balance - self.amount)


class UPI(Amazon):
    def __init__(self, balance, amount, upi_id):
        super().__init__(balance, amount)
        self.upi_id = upi_id

    def payment(self):
        upi_pin = input("Enter Your UPI Pin ")
        if self.amount > self.balance:
            print("Insufficient Account Balance!")
            return
        print("\nPayment is successful!")
        print("Remaining Account Balance:", self.balance - self.amount)

class credit_card(Amazon):
    def __init__(self, balance, amount, card_details):
        super().__init__(balance, amount)
        self.card_details = card_details

    def payment(self):
        otp = input("Enter OTP: ")
        if self.amount > self.balance:
            print("Insufficient Account Balance!")
            return
        print("\nPayment is successful!")
        print("Remaining Credit Balance:", self.balance - self.amount)

payment_option = input("Enter 1 for AmazonPay, 2 for UPI, 3 for Card: ")

if payment_option == "1":
    user = AmazonPayBalance(int(input("Enter Balance: ")),int(input("Enter Amount: ")),int(input("Enter Phone Number: ")))
elif payment_option == "2":
    user = UPI(int(input("Enter Balance: ")),int(input("Enter Amount: ")),input("Enter UPI ID: "))
elif payment_option == "3":
    user = credit_card(int(input("Enter Balance: ")),int(input("Enter Amount: ")),input("Enter Card Details: "))
else:
    print("Invalid option")
    user = None

if user:
    user.payment()

# 19. Create a Vehicle class and Car, Bike subclasses. Override max-speed().
class Vehicle:
    def __init__(self, model):
        self.model = model

    def max_speed(self):
        pass

class Car(Vehicle):
    def __init__(self, model):
        super().__init__(model)

    def max_speed(self):
        return 80

class Bike(Vehicle):
    def __init__(self, model):
        super().__init__(model)


    def max_speed(self):
        return 90

c = Car("Bolero")
print(c.max_speed())
b = Bike("KTM")
print(b.max_speed())


# 20. Implement Operator Overloading: add two objects of BankAccount to return total balance.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

acc1 = BankAccount(100)
acc2 = BankAccount(200)

print(acc1 + acc2)

# 21. Build a ShoppingCart class implementing add, remove, apply-discount.
class ShoppingCart:
    def __init__(self, item, price):
        self.cart = []
        self.price = 0

    def add_product(self, item, price):
        self.cart.append(item)
        self.price += price

    def remove_product(self, item, price):
        self.cart.remove(item)
        self.price -= price

    def apply_discount(self):
        self.price = self.price * 0.9 # 10% discount

    def total(self):
        return self.cart, self.price

cart = ShoppingCart([], 0)
cart.add_product("Milk", 30)
cart.add_product("Bread", 40)
cart.add_product("Eggs", 60)
cart.remove_product("Milk", 30)
cart.apply_discount()
print(cart.total())


# 22. Create a Library class to store books and a method to search by title or author.
class library:
    def __init__(self, books):
        self.books = books

    def store_books(self, book_name, author_name):
        book_details = (book_name, author_name)
        self.books.append(book_details)

    def search_book(self, book_name, author_name):
        for i in self.books:
            if i[0] == book_name or i[1] == author_name:
                return f"Found the book at index {self.books.index(i)+1}"
        return "Book does not exist"

l = library([("Charlotte's Web", "E.B. White")])
l.store_books("The Alchemist", "Paulo Coelho")
l.store_books("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
print(l.search_book("The Alchemist", None))
print(l.search_book(None, "E.B. White"))

# 23. Create a User class and an Admin subclass that can delete a user (override methods).
class User:
    def __init__(self, username):
        self.username = username

    def delete_user(self, target_user):
        return f"Regular users cannot delete other users."


class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    # Override delete_user method
    def delete_user(self, target_user):
        return f"Admin {self.username} deleted user {target_user.username}."

u1 = User("Alice")
u2 = User("Bob")
admin = Admin("SuperAdmin")

print(u1.delete_user(u2))
print(admin.delete_user(u2))