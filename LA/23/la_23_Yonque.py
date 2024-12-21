#la_23_Yonque
class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def intro_deco(self, func_name):
        def introduce(*args, **kwargs):
            print(f"Introducting {self.name}...")
            func_name(*args, **kwargs)
            print("This character is amazing!")
        return introduce
        
gojo_satoru = AnimeCharacter("Gojo Satoru", "Hollow Purple")

@gojo_satoru.intro_deco

def character_intro():
    print(f"I am {gojo_satoru.name} and I can use {gojo_satoru.ability}")
character_intro()