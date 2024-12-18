#oe_4
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self, target):
        target.health = target.health - self.atk_pwr
        print(f"({target.name}'s {target.health} HP has been damaged by {self.atk_pwr} attack power.")
    def special_move(self):
        pass
    def defend(self, attacker):
        attacker.power = attacker.power - 50
        print("Shield on.")
    
class Warrior(Character):
    def special_move(self, target): 
        target.health = target.health - self.power
        print(f"Warrior {self.name} uses Shield Bash on {target.name}! \n>> {target.name}'s health reduced by {self.power}. Total {target.name}'s HP: {target.health}")
        self.power = self.power * 2
        #double its attack power for the next attack 
        
class Mage(Character):
    def special_move(self, target):
        target.health = target.health - self.power
        print(f"Mage {self.name} casts Fireball on {target.name}! \n>> {target.name} HP - {self.power}. Total {target.name}'s HP: {target.health}")
        
class Archer(Character):
    def special_move(self, target):
        target.health = target.health - self.power
        print(f"Archer {self.name} shoots a Piercing Arrow on {target.name}! \n>> {target.name} health reduced by {self.power}. Total {target.name}'s HP: {target.health}")
        #ignores the target's defense (for bonus)
        
class Monster(Character):
    def __init__(self, name, health, power, heal, target):
        super().__init__(name, health, power)
        self.heal = heal
        self.target = target
    def special_move(self, heal, target):
        target.health = target.health - self.power
        self.health += self.heal
        print(f"Monster {self.name} roared to {target.name}")
        print(f">> Monster {self.name} dealt {self.power} damage to {target.name} and gained {self.heal} health! Total {self.name}'s HP: {self.health}")

warriorAtk = Warrior("Lapu Lapu", 1200, 150)
mageAtk = Mage("Eudora", 800, 200)
archerAtk = Archer("Miya", 900, 120)
monsterAtk = Monster("Helcurt", 1000, 80, 50, 80)

for x in (warriorAtk, mageAtk, archerAtk):
    x.special_move(monsterAtk)
    
for targets in (warriorAtk, mageAtk, archerAtk):
    monsterAtk.special_move(monsterAtk, targets)