# Example1: Device → Computer → Laptop

class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"[Device] {self.brand} device powering on.")


class Computer(Device):
    def __init__(self, brand, cpu):
        super().__init__(brand)
        self.cpu = cpu

    def boot(self):
        print(f"[Computer] Booting {self.brand} with CPU: {self.cpu}")


class Laptop(Computer):
    def __init__(self, brand, cpu, battery_level=100):
        super().__init__(brand, cpu)
        self.battery_level = battery_level

    def power_on(self):
        if self.battery_level <= 0:
            print("[Laptop] Battery drained! Please charge.")
        else:
            print(f"[Laptop] Powering on. Battery: {self.battery_level}%")
            super().power_on()

l = Laptop("HP", "Intel i7", 75)
l.power_on()
l.boot()


# Example 2: Animal → Mammal → Dog

class Animal:
    def speak(self):
        print("[Animal] Generic sound.")

class Mammal(Animal):
    def warm_blooded(self):
        print("[Mammal] I am warm-blooded.")

class Dog(Mammal):
    def speak(self):
        print("[Dog] Woof!")


d = Dog()
d.warm_blooded()
d.speak()

