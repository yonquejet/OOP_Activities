#la_21
#update la_20 value
class silog:
    def __init__(self, ulam, sinangag, itlog):
        self.ulam = ulam
        self.sinangag = sinangag
        self.__itlog = itlog #private access modifier
    def __str__(self):
        return f"Ang ulam ko ay may {self.ulam}, {self.sinangag}, {self.__itlog}."
    def getter(self):
        return self.__itlog
    def setter(self, new_val):
        self.__itlog = new_val
    
bacsilog = silog("Bacon", "Sinangag", "Puting Itlog")
hamsilog = silog("Ham", "Sinangag", "Itlog")
siosilog = silog("Siomai", "Sinangag", "Itlog")

bacsilog.setter("Itlog Pula")
print(bacsilog.getter())