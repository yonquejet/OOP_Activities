#la_22_Yonque
class bday_party_themes:
    def __init__(self, theme, food1, food2):
        self.theme = theme
        self.food1 = food1
        self.food2 = food2
    def __secretDish(self):
        print(f"Secret dish: {self.food1} at {self.food2}")
    def foods(self):
        print(f"{self.theme}: Cake, Spaghetti, Carbonara")
        print("Special dish: Lumpiang Shanghai")
        self.__secretDish()

halloween = bday_party_themes("Halloween", "Powdered Milk", "Champorado")
christmas = bday_party_themes("Christmas", "Milo", "Cookies")
valentines = bday_party_themes("Valentines", "Chocolates", "Kanin")

for x in (halloween, christmas, valentines):
    print("")
    x.foods()
