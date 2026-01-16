# Create a class Mobile with attributes brand, model, storage. Add a method to upgrade storage.

class Mobile:
    def __init__(self, brand, model, storage):
        self.brand, self.model, self.storage = brand, model, storage
    
    def add_storage(self, size):
        self.storage += size
        print(f"New storage size: {self.storage}")
        
m = Mobile("iQOO", "9SE", 128)
print(f"Brand: {m.brand}\nModel: {m.model}\nStorage: {m.storage}")
m.add_storage(int(input("Enter storage size: ")))
