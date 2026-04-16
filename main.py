import time
import os

groccery_list = []

def clear_screen():
    # Clears the terminal for a cleaner look
    os.system('cls' if os.name == 'nt' else 'clear')

def UpdSequence():
    if not groccery_list:
        print("List is empty!")
        return

    for i, item in enumerate(groccery_list):
        print(f"[{i + 1}] {item}")

    try:
        option = int(input("Select the element to update: "))
        if 1 <= option <= len(groccery_list):
            new_val = input("What value would you like to change it to?: ")
            groccery_list[option - 1] = new_val
            print("Updated! Returning to menu...")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")
    time.sleep(1)

def DelSequence():
    if not groccery_list:
        print("List is empty!")
        return

    for i, item in enumerate(groccery_list):
        print(f"[{i + 1}] {item}")

    try:
        option = int(input("Select the element to delete: "))
        if 1 <= option <= len(groccery_list):
            groccery_list.pop(option - 1)
            print("Deleted! Returning to menu...")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")
    time.sleep(1)

def AddSequence():
    print("Type [ END ] to stop adding.")
    while True:
        item = input("Add grocery: ")
        if item.lower() == "end":
            break
        groccery_list.append(item)

def ShowList():
    clear_screen()
    print("--- Current List ---")
    for i, item in enumerate(groccery_list):
        print(f"[{i + 1}] {item}")
    input("\nPress Enter to go back...")

def MainLoop():
    while True:
        clear_screen()
        print("Welcome to the grocery list program!")
        print("[ ADD | SHOW | UPDATE | DELETE | EXIT ]")
        
        choice = input("Your choice: ").lower()

        if choice == "add":
            AddSequence()
        elif choice == "show":
            ShowList()
        elif choice == "update":
            UpdSequence()
        elif choice == "delete":
            DelSequence()
        elif choice == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command.")
            time.sleep(1)

if __name__ == "__main__":
    MainLoop()