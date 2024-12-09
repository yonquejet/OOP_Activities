# Define the classes for Dog, Cat, Bird, and Fish

class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} says: Bark!")

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} says: Meow!")

class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} says: Chirp!")

class Fish:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("...")  # Fish don't make a sound

# Create the objects as specified in the problem
dogObj = Dog("Shitzu")
catObj = Cat("Sphinx")
birdObj = Bird("Angry Bird")
fishObj = Fish("Tilapia")

# Function to demonstrate polymorphism
def animal_sounds(animal):
    animal.speak()

# Iterate through each object and call the speak method
for animal in (dogObj, catObj, birdObj, fishObj):
    animal_sounds(animal)
