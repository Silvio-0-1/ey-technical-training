class Car:
	def __int__(self, brand, model, price):
		self.brand = brand
		self.model = model
		self.price = price

	def display(self):
		print("Brand: ", self.brand)
		print("Model: ", self.model)
		print("Price: ", self.price)

# creating car objects		
car1 = Car("Toyota", "Fortuner", 45)
car2 = Car("Tesla", "Model 3", 350)

# displaying details
carl.display()
print()
car2.disptay()
print()
