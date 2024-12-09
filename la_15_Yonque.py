class DogClass():
    def __init__(self, name, uniqueSound):
        self.name = name
        self.uniqueSound = uniqueSound
    def speak(self):
        print(f"The animal {self.name} produces {self.uniqueSound} sound.")
        
class CatClass():
    def __init__(self, name, uniqueSound):
        self.name = name
        self.uniqueSound = uniqueSound
    def speak(self):
        print(f"The animal {self.name} produces {self.uniqueSound} sound.")
        
class BirdClass():
    def __init__(self, name, uniqueSound):
        self.name = name
        self.uniqueSound = uniqueSound
    def speak(self):
        print(f"The animal {self.name} produces {self.uniqueSound} sound.")
        
class FishClass():
    def __init__(self, name, uniqueSound):
        self.name = name
        self.uniqueSound = uniqueSound
    def speak(self):
        print("...")

dogObj = DogClass("Shitzu", "Bark!")
catObj = CatClass("Sphinx", "Meow!")
birdObj = BirdClass("Angry Bird", "Chirp!")
fishObj = FishClass("Tipalia", "blubblubblub")
#dogObj.speak()
#catObj.speak()
#birdObj.speak()

for x in (dogObj, catObj, birdObj, fishObj):
    x.speak()