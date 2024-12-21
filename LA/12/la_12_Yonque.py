#la_12
#parent class
class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        print(f"Toy: {self.name}, Price: {self.price}")

#child class
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price) #for using super(), no need for self

smartPhone = Car("Toyota", "1,000,000")
smartPhone.__str__()