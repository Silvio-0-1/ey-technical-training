class customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def is_eligible(self):
        return (True if self.age > 25 else False)
    
c = customer("Silvio", 23, "Kolkata")
print("Eligible" if c.is_eligible() else "Not eligible")
