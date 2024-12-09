class silog:
    def __init__(self, ulam, sinangag, itlog):
        self.ulam = ulam
        self.sinangag = sinangag
        self.itlog = itlog
    def __str__(self):
        return f"Ang ulam ko ay may {self.ulam}, {self.sinangag}, {self.itlog}."
    
bacsilog = silog("Bacon", "Sinangag", "Puting Itlog")
hamsilog = silog("Ham", "Sinangag", "Itlog")
siosilog = silog("Siomai", "Sinangag", "Itlog")

print(f"{bacsilog}\n {hamsilog}\n {siosilog}")