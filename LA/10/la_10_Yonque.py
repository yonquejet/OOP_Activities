#la_10
#parent class
class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"{self.brand} {self.model} uses {self.fuel_type} gas.")

#child class - inheriting parent class attributes
class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

car1 = Car("Toyota", "Corolla", "Gasoline")
car1.describeVehicle()
motor1 = Motorcycle("Yamaha", "YZF-R3", "Gasoline")
motor1.describeVehicle()