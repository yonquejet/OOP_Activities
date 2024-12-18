#oe_2
# Step 1: Create the Phone class
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"

# List to store phone objects
phone_list = []

# Step 2: Define methods for creating, modifying, and deleting phones

def addObject():
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    price = input("Enter phone price: ")
    new_phone = Phone(brand, model, price)
    phone_list.append(new_phone)
    print("Phone added successfully!")
    exit_confirmation()

def modifyObject():
    if len(phone_list) == 0:
        print("No phones available to modify.")
        exit_confirmation()
        return

    viewPhones()  # View list of phones first
    phone_id = int(input("Enter the phone number you want to modify: ")) - 1

    if 0 <= phone_id < len(phone_list):
        phone = phone_list[phone_id]
        print(f"Modifying: {phone}")
        phone.brand = input("Enter new phone brand: ") or phone.brand
        phone.model = input("Enter new phone model: ") or phone.model
        phone.price = input("Enter new phone price: ") or phone.price
        print("Phone updated successfully!")
    else:
        print("Invalid selection!")

    exit_confirmation()

def deleteObject():
    if len(phone_list) == 0:
        print("No phones available to delete.")
        exit_confirmation()
        return

    viewPhones()  # View list of phones first
    phone_id = int(input("Enter the phone number you want to delete: ")) - 1

    if 0 <= phone_id < len(phone_list):
        phone_list.pop(phone_id)
        print("Phone deleted successfully!")
    else:
        print("Invalid selection!")

    exit_confirmation()

# Helper function to display phones
def viewPhones():
    print("\n--- List of Phones ---")
    if len(phone_list) == 0:
        print("No phones available.")
    else:
        for i, phone in enumerate(phone_list, start=1):
            print(f"{i}. {phone}")
    print("----------------------")

# Step 6: Create the main menu

def menu_screen():
    print("\n" * 50)
    print("--- Simple Python Program ---")
    print("1. Create Object\n2. Modify Object\n3. Delete Object\n4. View Phones\n5. EXIT.")
    menu_input = input("What do you want to do?\n> ")
    
    if menu_input == "1":
        print("\n" * 50)
        addObject()
        
    elif menu_input == "2":
        if len(phone_list) == 0:
            print("\n" * 50)
            print("No phones to modify. Create a phone first!")
            exit_confirmation()
        else: 
            print("\n" * 50)
            modifyObject()
            
    elif menu_input == "3":
        if len(phone_list) == 0:
            print("\n" * 50)
            print("No phones to delete. Create a phone first!")
            exit_confirmation()
        else:
            print("\n" * 50)
            deleteObject()

    elif menu_input == "4":
        viewPhones()
        exit_confirmation()
    
    elif menu_input == "5":
        quit()

# Exit confirmation handling
def exit_confirmation():
    user_ans = input("Return to main menu? \n> YES\n> NO(exit the program)\n----------\n> ").upper()
    
    if user_ans == "YES":
        menu_screen()
    elif user_ans == "NO":
        quit()
    else:
        print(f"{user_ans} is an invalid input!")
        exit_confirmation()

# Program start
menu_screen()
