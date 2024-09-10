#la_3_Yonque
class mobileLegends:
    def __init__(self,heroName):
        self.heroName = heroName
        
    def describe(self, heroRole, dmg_type): #method na to
        print(f"{self.heroName} is a {heroRole} that deals {dmg_type} damage.")
        
hero = mobileLegends("Terizla")
hero.describe("Fighter", "Physical")
hero = mobileLegends("Kagura")
hero.describe("Mage", "Magic")