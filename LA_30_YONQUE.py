import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")
root.configure(bg="#9999FF")
faveAnime = "Attack on Titan"

counter = 0
def display_text():
    global counter
    print(f"{counter}. My favorite anime is {faveAnime}.")
    counter += 1

button = tk.Button(root, text="RUN", command=display_text)
#walang open-close parentheses ang command=display_text para di magrun unless ipress
button.grid(row=0, column=0, padx=230, pady =100)

root.mainloop()