#la_24_Yonque
from abc import ABC, abstractmethod
class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print(f"{self.name} Swings sword!")

class Mage(GameCharacter):
    def attack(self):
        print(f"{self.name} Casts a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print(f"{self.name} Shoots an arrow!")

class Healer(GameCharacter):
    def attack(self):
        print(f"{self.name} Casts healing spell on ally!")

Explaner = Warrior("Lapu")
Midlaner = Mage("Nana")
Goldlaner = Archer("Miya")
Roam = Healer("Rafaela")
#polymorphism
for x in (Explaner, Midlaner, Goldlaner, Roam):
    x.attack()