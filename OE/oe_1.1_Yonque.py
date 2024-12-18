#oe_1
class hero:
    def __init__(self, heroName, heroRole, dmg_type):
        self.heroName = heroName
        self.heroRole = heroRole
        self.dmg_type = dmg_type
        
    def teamDescription(self, heroRole, dmg_type): #method
        print(f"{self.heroName} is a {heroRole} that deals {dmg_type} damage.")
        
    def __str__(self):
        return(f"{self.heroName} is a {self.heroRole} that deals {self.dmg_type} damage.")

#printing __init__
battle_hero1 = hero("Layla", "Marksman", "Physical")
print(f"{battle_hero1.heroName} is a {battle_hero1.heroName} that deals {battle_hero1.dmg_type} damage.")

#printing method
battle_hero2 = hero("Kagura", ".", ".") #di na need lagyan second 
battle_hero2.teamDescription("Mage", "Magic") 

#printing __str__
battle_hero = hero("Lapu lapu", "Fighter", "Physical")
print(battle_hero)


