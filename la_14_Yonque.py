#la_14
class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describeSpiderman(self):
        print(f"Spiderman {self.name} is {self.age} years old.")
    
class Tobey(Spiderman):
    def __init__(self, name, movieTitle):
        super().__init__(name, movieTitle)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, movieTitle):
        super().__init__(name, movieTitle)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, movieTitle):
        super().__init__(name, movieTitle)
        self.movieTitle = movieTitle

spidey1 = Tobey("Tobey Maguire", "Spider-Man trilogy")
spidey2 = Andrew("Andrew Garfield", "Amazing spiderman 1 & 2")
spidey3 = Tom("Tom Holland", "Spiderman: No way home")
print(f"{spidey1.name.upper()} is an actor in {spidey1.movieTitle}")
print(f"{spidey2.name.upper()} is an actor in {spidey2.movieTitle}")
print(f"{spidey3.name.upper()} is an actor in {spidey3.movieTitle}")
