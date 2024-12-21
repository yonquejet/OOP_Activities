#la_11
#parent class
class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describePhone(self):
        print(f"{self.brand}, {self.model}")

#child class
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self,brand,model)

smartPhone = Android("Infinix", "Note 11s")
smartPhone.describePhone()