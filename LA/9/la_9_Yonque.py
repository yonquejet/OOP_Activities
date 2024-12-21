#la_9
class Car:
    def __init__(self, brand):
        self.brand = brand
        
    def __str__(self):
        return (f"{self.brand} is a car brand.")
        
    
kotse = Car("Honda")
print(kotse.brand)
print(kotse)

del kotse
#print(kotse)


