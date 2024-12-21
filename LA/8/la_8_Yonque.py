#la_8
class Book:
    def __init__(self, title, author):
        self.title = title #instantializing, now attributes
        self.author = author
        
libro = Book("Atomic Habits", "James Clear") #object
new_libro = Book("48 laws of power", "Robert Greene") #object
print(f"Original values: {libro.title} and {libro.author}")

del libro.author
#print(f"Original values: {libro.title} and {libro.author}")

libro.author = "James Clear"
print(f"Original values: {libro.title} and {libro.author}")

print(f"Updated values: {new_libro.title} and {new_libro.author}")
