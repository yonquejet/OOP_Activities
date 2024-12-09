class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def operate(self):
        print("Operating!")
        
    def method_info(self):
        print(f"This appliance brand {self.brand} uses {self.model}.")

class WashingMachine(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Washing clothes!")
class Refrigerator(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Keeping food cold!")
class Microwave(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Heating food!")

wmObj = WashingMachine("Fujidenzo", "BWS-780")
fridgeObj = Refrigerator("Samsung", "Model-69")
mwObj = Microwave("Samsung", "Model-5")


for x in (wmObj, fridgeObj, mwObj):
    x.operate()