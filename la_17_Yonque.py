#la_17
#create loop with condition na panalo ang 0 ang health
class Player:
    def __init__(self, name, health, atk_pwr):
        self.name = name
        self.health = health
        self.atk_pwr = atk_pwr
    def attack(self, target):
        target.health = target.health - self.atk_pwr
        print(f"{target.name}'s {target.health} HP has been damaged by {self.atk_pwr} attack power.")
    def heal(self, amount):
        self.health = self.health + amount
        print(f"{self.name} has been healed {amount} totalling {self.health}.")
    
player1 = Player("Player 1", 10000, 500)
player2 = Player("Player 2", 5000, 250)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2) 
    player2.attack(player1)

if player1.health > player2.health:
    print(f"{player1.name} has won with a {player1.health} HP left.")
    player1.heal(300)
    print(f"{player1.name} has won with a {player1.health} HP left.")
if player2.health > player1.health:
    print(f"{player2.name} has won with a {player2.health} HP left.")
    player2.heal(300)
    print(f"{player2.name} has won with a {player2.health} HP left.")

#players = [player1, player2]





    