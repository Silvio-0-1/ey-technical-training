class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_cost(self):
        return self.price * self.quantity
    
p = product("Milk", 29.5, 2)
print(p.calculate_cost())
