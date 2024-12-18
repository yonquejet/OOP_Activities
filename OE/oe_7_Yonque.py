#oe_7
class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability 
    def introduce(ramdom_parameter, some_function):
        def inner():
            print("Introducing...")
            some_function()
            print("This character is amazing!")
        return inner
        
nina = TekkenCharacter("Nina", "Fatal Judgement")

@nina.introduce
def character_intro():
    print(f"I am {nina.name} and I can use {nina.ability}")
        
character_intro()
        


    