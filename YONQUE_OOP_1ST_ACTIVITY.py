#oop example, mobile legends
class hero():
    def __init__(self,name,role,dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
        
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"

hero_mm1 = hero("natan", "marksman", "magic dmg", 2450, 116) 
hero_fighter1 = hero("aldous", "fighter", "atk dmg", 2718, 129)
hero_jungler1 = hero("ling", "jungler", "atk dmg", 2528, 125)
hero_roamer1 = hero("atlas", "roam", "atk dmg", 2759, 129)
hero_midlaner1 = hero("luo yi", "midlaner", "magic dmg", 2601, 107)

print(f'''
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_mm1.dmg_type}
{hero_mm1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health} HP
{hero_fighter1.auto_atk_dmg} basic attack damage
{hero_fighter1.dmg_type}
{hero_fighter1.describe()} 

{hero_jungler1.name}
{hero_jungler1.role}
{hero_jungler1.health} HP
{hero_jungler1.auto_atk_dmg} basic attack damage
{hero_jungler1.dmg_type}
{hero_jungler1.describe()}

{hero_roamer1.name}
{hero_roamer1.role}
{hero_roamer1.health} HP
{hero_roamer1.auto_atk_dmg} basic attack damage
{hero_roamer1.dmg_type}
{hero_roamer1.describe()}

{hero_midlaner1.name}
{hero_midlaner1.role}
{hero_midlaner1.health} HP
{hero_midlaner1.auto_atk_dmg} basic attack damage
{hero_midlaner1.dmg_type}
{hero_midlaner1.describe()}''')
