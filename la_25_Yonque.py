#la_25
from abc import ABC, abstractmethod
class Character(ABC): #abstract class
    @property
    @abstractmethod #decorator
    def alias(self): #abstract property 
        pass

class Batman(Character):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias
    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"

Bruce_Wayne = Batman("Bruce Wayne", "Batman")
print(Bruce_Wayne.alias)