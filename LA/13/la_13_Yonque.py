#la_13
#parent class
class Animal():
    def __init__(self, name, type, can_swim):
        self.name = name
        self.type = type
        #self.can_swim = can_swim
        
    def describeAnimal(self):
        print(f"{self.name} is a {self.type} that can swim, {self.can_swim}")

#child class
class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type, can_swim)
        self.can_swim = True #or false

x = Fish("Nemo", "Goldfish", True) #or false)
x.describeAnimal()