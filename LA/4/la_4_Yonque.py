#la_4_Yonque
class mobileLegends:
    def __init__(self,heroName, heroRole, dmg_type):
        self.heroName = heroName
        self.heroRole = heroRole
        self.dmg_type = dmg_type
        
    def describe(self, heroRole, dmg_type): #method
        print(f"{self.heroName} is a {heroRole} that deals {dmg_type} damage.")
        
    def __str__(self): #string manipulation
        return (f"{self.heroName} is a {self.heroRole} that deals {self.dmg_type} damage.")
    
hero = mobileLegends("Zilong", "Fighter", "Physical")
#hero.describe("Fighter", "Physical")
hero = mobileLegends("Kagura", "Mage", "Magic" )
#hero.describe("Mage", "Magic")

print(f"{hero.heroName} is a {hero.heroRole} that deals {hero.dmg_type} damage")
print(hero)#string manipulation