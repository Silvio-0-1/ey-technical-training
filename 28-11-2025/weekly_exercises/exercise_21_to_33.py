# 26. Create a class Book with title, author, pages. Add method to check if pages > 300.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def check(self):
        if self.pages > 300:
            print("Pages are more than 300")
        else:
            print("Pages are less than 300")

b = Book("You Can Win", "Shiv Khera", 350)
b.check()

# 28. Create a class Rectangle with methods to calculate area and perimeter.
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area: ", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter: ", 2*(self.length + self.breadth))

rect = rectangle(10,5)
rect.area()
rect.perimeter()

# 33. Create a class Laptop and a method to calculate discount
class laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

    def display(self):
        print("Brand: ", self.brand)
        print("RAM: ", self.ram)
        print("Processor: ", self.processor)
        print("Price: ", self.price)

    def discount(self):
        print("After 10% Discount: ", round(float(self.price - 0.1 * self.price), 2))

l = laptop("Acer", "16 GB", "i7", 65000)
l.display()
l.display()
l.discount()