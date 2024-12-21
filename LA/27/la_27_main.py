#la_27 boilerplate
import la_27_Yonque as main

Leonardo = main.Leonardo("Leonardo", "L")
Michaelangelo = main.Michaelangelo("Michaelangelo", "M")
Donatello = main.Donatello("Donatello", "D")
Raphael = main.Raphael("Raphael", "R")

print(Leonardo.alias)
print(Michaelangelo.alias)
print(Donatello.alias)
print(Raphael.alias)

if __name__ == "__main__":
    Leonardo = main.Leonardo("Leonardo Decaprio", "Leo")
    print(Leonardo.alias)