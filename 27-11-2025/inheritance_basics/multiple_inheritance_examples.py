# Example 1: HybridCar ← ElectricVehicle + FuelVehicle

class ElectricVehicle:
    def charge(self, kwh):
        print(f"[EV] Charging {kwh} kWh.")

    def drive(self):
        print("[EV] Driving using electric motor.")


class FuelVehicle:
    def refuel(self, liters):
        print(f"[Fuel] Refueled {liters} liters.")

    def drive(self):
        print("[Fuel] Driving using combustion engine.")


class HybridCar(ElectricVehicle, FuelVehicle):
    def drive(self, mode="auto"):
        if mode == "electric":
            ElectricVehicle.drive(self)
        elif mode == "fuel":
            FuelVehicle.drive(self)
        else:
            print("[Hybrid] Auto mode: choosing best power source.")


hy = HybridCar()
hy.charge(20)
hy.refuel(10)
hy.drive("electric")
hy.drive("fuel")
hy.drive()
print(HybridCar.mro())  # Method Resolution Order

# the MRO decides which parent’s method is used first. Here, `ElectricVehicle` is checked before `FuelVehicle`

# Example 2: DataScientist ← Programmer + Statistician

class Programmer:
    def code(self, language):
        print(f"[Programmer] Writing code in {language}.")

    def profile(self):
        return {"skill": "programming"}


class Statistician:
    def analyze(self, dataset):
        print(f"[Statistician] Analyzing dataset: {dataset}")

    def profile(self):
        return {"skill": "statistics"}


class DataScientist(Programmer, Statistician):
    def profile(self):
        p1 = Programmer.profile(self)
        p2 = Statistician.profile(self)
        return {**p1, **p2, "role": "Data Scientist"}


ds = DataScientist()
ds.code("Python")
ds.analyze("sales.csv")
print(ds.profile())
