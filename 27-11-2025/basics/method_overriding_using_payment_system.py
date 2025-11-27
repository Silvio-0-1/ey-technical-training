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
