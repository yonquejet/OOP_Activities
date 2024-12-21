#la_7
class Car:
    def __init__(self, brand, color):
        self.brand = brand #instantializing, now attributes
        self.color = color
        
car_object = Car("Toyota", "Gray") #object
print(f"Original values: {car_object.brand} and {car_object.color}")

car_object.color = "Black" #updating value
print(f"Original values: {car_object.brand} and {car_object.color}")

car_object2 = Car("Honda", "Blue") #new object
print(f"Updated values: {car_object2.brand} and {car_object2.color}")