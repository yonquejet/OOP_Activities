#la_2_yonque
class mobileLegends:
    def __init__(self, heroName, heroRole):
        self.heroName = heroName
        self.heroRole = heroRole
        
hero1 = mobileLegends("Zhuxin", "Mage")
hero2 = mobileLegends("Johnson", "Tank")

print(f"{hero1.heroName}'s role is {hero1.heroRole}.")
print(f"{hero2.heroName}'s role is {hero2.heroRole}.")
