import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")
root.configure(bg="#9999FF")

myName = "Jetlee_Yonque"
mySection = "BSIT-2A"

hello = tk.Label(root, text=f"OOP LA29 {myName} {mySection}")
hello.grid(row=0, column=0, padx=160, pady=100)

root.mainloop()