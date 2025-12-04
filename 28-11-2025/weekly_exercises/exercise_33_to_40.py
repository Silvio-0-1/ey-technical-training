# 34. Create parent class Vehicle and child class Car that overrides a method start()
class Vehicle:
    def start(self):
        print("Starting the vehicle")

class Tesla(Vehicle):
    def start(self):
        print("Starting using battery")

t = Tesla()
t.start()


# 35. Create Person → Employee → Manager (multilevel). Add different methods in each
class person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class employee(person):
    def __init__(self, name, gender, id):
        super().__init__(name, gender)
        self.id = id

class manager(employee):
    def __init__(self, name, gender, id, rank):
        super().__init__(name, gender, id)
        self.rank = rank

    def print(self):
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("ID: ", self.id)
        print("Rank: ", self.rank)

m = manager("X", "M", 10021, 1)
m.print()


# 40. Create a class Score that overloads the + operator to combine two scores, and overloads > to compare them
